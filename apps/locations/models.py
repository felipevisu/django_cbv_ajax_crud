from django.db import models

class City(models.Model):
    name = models.CharField('nome', max_length=150)

    def __str__(self):
        return self.name


class Sector(models.Model):
    name = models.CharField('nome', max_length=150)
    city = models.ForeignKey(City, related_name='sectors', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Neighborhood(models.Model):
    name = models.CharField('nome', max_length=150)
    sector = models.ForeignKey(Sector, related_name='neighborhoods', on_delete=models.CASCADE)

    def __str__(self):
        return self.name
