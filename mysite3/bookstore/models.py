from django.db import models


# Create your models here.

class Book(models.Model):
    # 字段名 = models.字段类型（字段选项）
    title = models.CharField("书名", max_length=50, default='', unique=True)
    price = models.DecimalField("定价", max_digits=7, decimal_places=2, default=0.0)
    pub = models.CharField("出版社", max_length=100, default='')
    # info = models.CharField('描述', max_length=100, default='')
    market_price = models.DecimalField("零售价", max_digits=7, decimal_places=2, default=0.0)
    is_active = models.BooleanField('是否活跃', default=True)

    class Meta:
        db_table = 'book'  # 改表名

    def __str__(self):
        return '%s_%s_%s_%s' % (self.title, self.price, self.market_price, self.pub)


class Author(models.Model):
    name = models.CharField("姓名", max_length=11, default='')
    age = models.IntegerField("年龄", default=1)
    email = models.EmailField("邮箱", null=True)

    class Meta:
        db_table = 'author'
