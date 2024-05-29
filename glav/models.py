from django.db import models


class Land(models.Model):
    name_land = models.CharField(max_length=62)
    population_land = models.IntegerField()
    flag = models.ImageField()

    def __str__(self):
        return f'{self.name_land}'


class Capital(models.Model):
    land = models.OneToOneField(Land, on_delete=models.CASCADE, null=True, blank=True)
    name_capital = models.CharField(max_length=62)
    population_capital = models.IntegerField()
    short_description = models.TextField()
    img_capital = models.ImageField()


    def __str__(self):
        return f'{self.name_capital} '
