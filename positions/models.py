from django.db import models


class Test(models.Model):
    name = models.CharField(max_length=200)
    code = models.CharField(max_length=15)

    def __str__(self):
        return self.name


class Position(models.Model):
    name = models.CharField(max_length=200)
    image = models.URLField()
    price = models.CharField(max_length=10)
    rank = models.CharField(max_length=10)
    market_cap = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['rank']
