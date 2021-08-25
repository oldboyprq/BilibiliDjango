from django.db import models


# Create your models here.
class Pub(models.Model):
    name = models.CharField('出版社', max_length=50)


class Book(models.Model):
    title = models.CharField('书名',max_length=11)
    pub = models.ForeignKey(Pub,on_delete=models.CASCADE)