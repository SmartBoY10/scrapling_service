from django.db import models

class City(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название города')
    slug = models.SlugField(max_length=50, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Город'
        verbose_name_plural = 'Городы'
    
