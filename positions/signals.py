# from django.db.models.signals import post_save
# from django.dispatch import receiver
#
# from .models import Test
# from .tasks import create_code
#
#
# @receiver(post_save, sender=Test)
# def set_code(sender, instance, created, *args, **kwargs):
#     if created:
#         create_code.delay()
