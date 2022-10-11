from django.db import models
from versatileimagefield.fields import VersatileImageField, PPOIField


class Brand(models.Model):
    """
    Marca de un automóvil
    """
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name

class Group(models.Model):
    """
    Grupo o modelo de un automóvil
    """
    CAR = 1
    PICKUP = 2
    COMMERCIAL = 3
    SUV = 4
    CROSSOVER = 5
    categories = (
        (CAR, 'Auto'),
        (PICKUP, 'Pickup'),
        (COMMERCIAL, 'Comercial'),
        (SUV, 'Suv'),
        (CROSSOVER, 'Crossover'),
    )
    name = models.CharField(max_length=255)
    category = models.PositiveSmallIntegerField(choices=categories, null=True,
                                                blank=True)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('name', 'brand')

    def __str__(self):
        return self.name

class Version(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    photo = VersatileImageField( upload_to='static/images/cars', ppoi_field='photo_ppoi',
                                 null=True, blank=True, max_length=200,
                                 help_text='Foto del automóvil'
                                 )
    photo_ppoi = PPOIField('Image PPOI')

    def __str__(self):
        return '{},{},{}'.format(self.group.brand.name, self.group.name, self.name)

class Price(models.Model):
    year = models.IntegerField()
    price = models.IntegerField(null=True)
    version = models.ForeignKey(Version, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('version', 'year')
