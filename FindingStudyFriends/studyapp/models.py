from django.db import models


class Store(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)


class Category(models.Model):
    first = models.CharField(max_length=200)
    second = models.CharField(max_length=200)