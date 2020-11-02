from django.db import models


class Story(models.Model):
    protagonist = models.CharField(max_length=30)
    antagonist = models.CharField(max_length=30)
    setting = models.CharField(max_length=30)
    SETTING_CHOICES = (
        ('spc', 'SPACE'),
        ('wstrn', 'WESTERN'),
        ('ar', 'ANCIENT ROME'),
        ('dysf', 'DYSTOPIA FUTURE')
    )
    plot = models.CharField(max_length=30)
    conflict = models.CharField(max_length=30)
    genre = models.CharField(max_length=60)
