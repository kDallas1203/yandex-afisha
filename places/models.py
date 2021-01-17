from django.db import models


class Place(models.Model):
    title = models.CharField(max_length=150, verbose_name="Название места")
    description_short = models.CharField(max_length=255, verbose_name="Короткое описание")
    description_long = models.TextField(verbose_name="Описание")
    lng = models.FloatField(verbose_name="Долгота")
    lat = models.FloatField(verbose_name="Широта")

    def __str__(self):
        return self.title
