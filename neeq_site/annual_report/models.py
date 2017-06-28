from django.db import models

# Create your models here.
class Report(models.Model):
    code = models.CharField(verbose_name="代码", max_length=10)
    name = models.CharField(verbose_name="简称", max_length=10)
    induestry = models.CharField(verbose_name="行业", max_length=20)
    year = models.CharField(verbose_name="年份", max_length=5)
    content = models.TextField(verbose_name="年报内容", blank=True, null=True)