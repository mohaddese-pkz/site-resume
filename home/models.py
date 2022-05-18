from django.db import models

class Info(models.Model):
    name = models.CharField(verbose_name='name', max_length=60)
    img = models.ImageField(verbose_name='image', upload_to='images/',null=True)
    desc = models.TextField(verbose_name='description')
    city = models.CharField(verbose_name='city', max_length=60)


class Work(models.Model):
    year = models.IntegerField(verbose_name='year',null=True)
    company = models.CharField(verbose_name='company', max_length=60,null=True)
    job = models.CharField(verbose_name='job', max_length=60,null=True)

class Award(models.Model):
    date_a = models.TextField(verbose_name='date',null=True)
    desc_a = models.TextField(verbose_name='description',null=True)

class Skill(models.Model):
    date_s = models.TextField(verbose_name='date',null=True)
    field = models.CharField(verbose_name='field', max_length=60,null=True)
    skill = models.TextField(verbose_name='skill',null=True)
