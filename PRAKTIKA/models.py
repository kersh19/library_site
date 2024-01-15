from datetime import date
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.urls import reverse
from django.http import HttpResponse
from PIL import Image
from phonenumber_field.modelfields import PhoneNumberField
SHORT_TEXT_LEN = 300
class Poln_text(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название')
    silka = models.CharField(max_length=20000, verbose_name='Ссылка на сайт')
    text = models.TextField(verbose_name='Текст')
    studtxt = models.TextField( blank=True, verbose_name='Для студента')
    preptxt = models.TextField( blank=True, verbose_name='Для преподавателя')
    vsetxt = models.TextField( blank=True, verbose_name='Общая')
    slug = models.SlugField(verbose_name='Хранение изображения', null=True)
    image = models.ImageField(upload_to='text', null=True)
    stud = models.FileField(upload_to='books/', blank=True, verbose_name='Для студента')
    prep = models.FileField(upload_to='books/', blank=True, verbose_name='Для преподавателя')
    vse = models.FileField(upload_to='books/', blank=True, verbose_name='Общая')
    def __str__(self):
        return self.title
    def get_short_text(self):
        if len(self.text) > SHORT_TEXT_LEN:
            return self.text[:SHORT_TEXT_LEN]
        else:
            return self.text
    @property
    def image_url(self):
        if self.image and hasattr(self.image, 'url'):
            return self.image.url
    class Meta:
        verbose_name = 'Полнотекстовый ресурс'
        verbose_name_plural = 'Полнотекстовые ресурсы'
class News(models.Model):  # artist album
    title = models.CharField(max_length=200, verbose_name='Название')
    text = models.TextField(verbose_name='Текст')
    slug = models.SlugField(verbose_name='Хранение изображения')
    image = models.ImageField(upload_to='nws')
    def __str__(self):
        return self.title
    def get_short_text(self):
        if len(self.text) > SHORT_TEXT_LEN:
            return self.text[:SHORT_TEXT_LEN]
        else:
            return self.text
    @property
    def image_url(self):
        if self.image and hasattr(self.image, 'url'):
            return self.image.url
    class Meta:
        verbose_name = 'Новости'
        verbose_name_plural = 'Новости'
class Exhibition_tema(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название')
    text = models.TextField(verbose_name='Текст')
    data_exhib = models.TextField(verbose_name='Дата проведения выставки')
    slug = models.SlugField(verbose_name='Хранение изображения', null=True)
    image = models.ImageField(upload_to='exh', null=True)
    def __str__(self):
        return self.title
    def get_short_text(self):
        if len(self.text) > SHORT_TEXT_LEN:
            return self.text[:SHORT_TEXT_LEN]
        else:
            return self.text
    @property
    def image_url(self):
        if self.image and hasattr(self.image, 'url'):
            return self.image.url
    class Meta:
        verbose_name = 'Тематическая выставка'
        verbose_name_plural = 'Тематические выставки'
class Tags(models.Model):  # genre
    name = models.CharField(max_length=100, verbose_name='Новинки')
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Новинкa'
        verbose_name_plural = 'Новинки'
class Kontakt(models.Model):
    name = models.CharField(max_length=255, verbose_name='ФИО', blank=True)
    dol = models.CharField(max_length=255, verbose_name='Должность')
    phoneNumber = PhoneNumberField(unique = True, null = False, blank = False) # Here
    secondPhoneNumber = models.TextField(max_length=4, verbose_name='Bнутренний') # Here
    mail = models.CharField(max_length=255, verbose_name='Электронная почта', blank=True)
    mesto = models.CharField(max_length=255, verbose_name='Место работы', blank=True)
    def __str__(self):
        return self.dol
    class Meta:
        verbose_name = 'Работник'
        verbose_name_plural = 'Работники'
class Exh_nov_iz(models.Model):
    category = models.ManyToManyField(Tags, verbose_name='Категория')
    title = models.TextField(max_length=255, verbose_name='Краткое описание')
    text = models.TextField(verbose_name='Текст')
    slug = models.SlugField(verbose_name='Хранение изображения', null=True)
    image = models.ImageField(upload_to='exh', null=True)
    def __str__(self):
        return self.title
    @property
    def image_url(self):
        if self.image and hasattr(self.image, 'url'):
            return self.image.url
    class Meta:
        verbose_name = 'Новинка издательства'
        verbose_name_plural = 'Новинки издательств'
class Date(models.Model):
    dat = models.DateField(verbose_name='Дата события')
    title = models.TextField(max_length= 255, verbose_name='Название')
    text = models.TextField(verbose_name='Описание')
    slug = models.SlugField(verbose_name='Хранение изображения', null=True)
    image = models.ImageField(upload_to='exh', null=True)
    def __str__(self):
        return self.title
    @property
    def is_past_due(self):
        return date.today() < self.date
    @property
    def image_url(self):
        if self.image and hasattr(self.image, 'url'):
            return self.image.url
    class Meta:
        verbose_name = 'Календарь'
        verbose_name_plural = 'Календари'