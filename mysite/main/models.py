from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    message = models.TextField()
    sent_at = models.DateTimeField(auto_now_add=True)
# class Person(models.Model):
#     name = models.CharField(max_length=50)
#     last_name = models.CharField(max_length=50)
#     gender = models.BooleanFild()
#     profession = models.CharField(max_length=50)

class Skill(models.Model):
    title = models.CharField(max_length=50, verbose_name="Заголовок")
    description = models.TextField(verbose_name="Описания")
    link = models.TextField(verbose_name='Ссылка')
    photo = models.ImageField(upload_to='main', blank=True, null=True, verbose_name='Изображения')
    sent_at = models.DateTimeField(auto_now_add=True, verbose_name='Время и Дата опубликования')

class My_Skill(models.Model):
    title = models.TextField(verbose_name = "Заголовок")
    # sent_at = models.DateTimeField(auto_now_add =True)