from django.db import models

class Task(models.Model):
    Category=[("l", 'Библиотека'),("5", '5класс'),("6", '6класс'),("8", '8класс'),('9', '9класс'),\
              ("7", '7класс'),("10", '10класс'),("11", "11класс")]
    article_type = models.CharField(max_length=2, choices=Category, default='l')
    title = models.CharField('Название', max_length = 50)
    task = models.TextField('Описание')


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

