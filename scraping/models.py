import jsonfield
from django.db import models

from scraping.utils import from_cyrillic_to_eng


def default_urls():
    return {"work": "", "dou": "", "djinni": ""}


class City(models.Model):
    name = models.CharField(max_length=50,
                            verbose_name='Назва населеного пункту',
                            unique=True)
    slug = models.CharField(max_length=50, blank=True, unique=True)
    
    class Meta:
        verbose_name = 'Назва населеного пункту'
        verbose_name_plural = 'Назви населених пунктів'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = from_cyrillic_to_eng(str(self.name))
        super().save(*args, **kwargs)


class Language(models.Model):
    name = models.CharField(max_length=50,
                            verbose_name='Мова програмування',
                            unique=True)
    slug = models.CharField(max_length=50, blank=True, unique=True)

    class Meta:
        verbose_name = 'Мова програмування'
        verbose_name_plural = 'Мови програмування'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = from_cyrillic_to_eng(str(self.name))
        super().save(*args, **kwargs)


class Vacancy(models.Model):
    url = models.URLField(unique=True)
    title = models.CharField(max_length=250, verbose_name='Заголовок вакансії')
    company = models.CharField(max_length=250, verbose_name='Компанія')
    description = models.TextField(verbose_name='Опис вакансії')
    city = models.ForeignKey('City', on_delete=models.CASCADE,
                             verbose_name='Місто', related_name='vacancies')
    language = models.ForeignKey('Language', on_delete=models.CASCADE,
                                 verbose_name='Мова програмування')
    timestamp = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = 'Вакансія'
        verbose_name_plural = 'Вакансії'
        ordering = ['-timestamp']

    def __str__(self):
        return self.title


class Error(models.Model):
    timestamp = models.DateField(auto_now_add=True)
    data = jsonfield.JSONField()

    def __str__(self):
        return str(self.timestamp)


class Url(models.Model):
    city = models.ForeignKey('City', on_delete=models.CASCADE,
                             verbose_name='Місто')
    language = models.ForeignKey('Language', on_delete=models.CASCADE,
                                 verbose_name='Мова програмування')
    url_data = jsonfield.JSONField(default=default_urls)

    class Meta:
        unique_together = ("city", "language")
