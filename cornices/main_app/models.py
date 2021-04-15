from django.db import models


class Contact(models.Model):
    phone_number = models.CharField(max_length=12)
    viber = models.CharField(max_length=12, blank=True)
    email = models.EmailField(blank=True)
    city = models.CharField(max_length=100, blank=True)
    street = models.CharField(max_length=255, blank=True)
    NIP = models.CharField(max_length=15, blank=True)
    REGON = models.CharField(max_length=15, blank=True)

    def __str__(self):
        return self.phone_number

    @property
    def address(self):
        return f'{self.street} {self.city}'

    class Meta:
        verbose_name = 'Dane kontaktowe'
        verbose_name_plural = 'Dane kontaktowe'


class PriceList(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name = 'Cennik'
        verbose_name_plural = 'Cennik'

