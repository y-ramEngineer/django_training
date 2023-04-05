from django.db import models

# Create your models here.
class SampleModel(models.Model):
    title = models.CharField(max_length=100)
    number = models.IntegerField()

CATEGORY = (('business', 'ビジネス'), ('life', '生活'), ('other', 'その他'))

class BlogModel(models.Model):
    title = models.CharField(max_length=100)

class BlogModel2(models.Model):
    title = models.CharField(max_length=100)
