from django.db import models


# Create your models here.


class Artical(models.Model):
    title = models.CharField('Название', max_length=50)
    anons = models.CharField('anons', max_length=250)
    full_text = models.TextField('Статя')
    date = models.DateTimeField('Дата публикации')
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'