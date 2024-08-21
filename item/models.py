from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(max_length=250)
    price = models.DecimalField(max_digits=9, decimal_places=2)
    
    class Meta:
        verbose_name = 'Позиция'
        verbose_name_plural = 'Позиции'

    def __str__(self):
        return self.name
