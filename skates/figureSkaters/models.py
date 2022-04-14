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


class Elements(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Skaters(models.Model):
    name = models.CharField(max_length=255)
    nation = models.ForeignKey(Nation, on_delete=models.PROTECT)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)

    def __str__(self):
        return self.name


class Points(models.Model):
    skater = models.ForeignKey(Skaters, on_delete=models.PROTECT)
    competition = models.ForeignKey(Competition, on_delete=models.PROTECT)
    segment = models.ForeignKey(Segment, on_delete=models.PROTECT)
    element = models.ForeignKey(Elements, on_delete=models.PROTECT)
    base_value = models.FloatField()
    GOE = models.FloatField()
    judges_score = models.TextField()
    total_score = models.FloatField()

    def __str__(self):
        return str(self.skater) + " " + str(self.element) + " " + str(self.total_score)


class Result(models.Model):
    position = models.IntegerField()
    skater = models.ForeignKey(Skaters, on_delete=models.PROTECT)
    nation = models.ForeignKey(Nation, on_delete=models.PROTECT)
    score = models.FloatField()
    SP = models.IntegerField()
    FS = models.IntegerField()
    competition = models.ForeignKey(Competition, on_delete=models.PROTECT)

    def __str__(self):
        return str(self.position) + " " + str(self.score)
