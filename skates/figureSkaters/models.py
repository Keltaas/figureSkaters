from django.db import models


class Nation(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Segment(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Competition(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
