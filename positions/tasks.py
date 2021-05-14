from celery import shared_task
from celery.decorators import periodic_task
from .models import Test
from celery.task.schedules import crontab

import requests

from .utils import create_random_code
from .models import Position


@shared_task
def get_crypto_info():
    url = 'https://api.coingecko.com/api/v3/coins/markets?vs_currency=USD&order=market_cap_desc&per_page=100&page=1&sparkline=false'
    data = requests.get(url).json()

    for item in data:
        p, c = Position.objects.get_or_create(name=item['name'])
        p.image = item.get('image')
        p.price = item.get('current_price')
        p.market_cap = item.get('market_cap')
        p.rank = item.get('market_cap_rank')
        p.save()


@periodic_task(run_every=crontab(minute='*/1'))
def update_crypto_info():
    get_crypto_info.delay()

# @shared_task
# def create_test_object(name):
#     return Test.objects.create(name=name)


# @shared_task
# def create_code():
#     codes = Test.objects.all()
#     for code in codes:
#         code.code = create_random_code()
#         code.save()
#
#
# @periodic_task(run_every=(crontab(minute='*/1')))
# def run_task_periodically():
#     return create_test_object.delay(name='new2020')
