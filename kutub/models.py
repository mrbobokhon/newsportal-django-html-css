from django.db import models
# Create your models here.


class Davlat(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Tuman(models.Model):
    davlat = models.ForeignKey(Davlat, on_delete=models.RESTRICT)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Kutubxona(models.Model):
    davlat = models.ForeignKey(Davlat, on_delete=models.RESTRICT)
    tuman = models.ForeignKey(Tuman, on_delete=models.RESTRICT, null=True, default=None)
    nomi = models.CharField(max_length=50)