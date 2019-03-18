from django.db import models

# Create your models here.
#登录
#登录
class User(models.Model):
    phone = models.CharField(max_length=40,unique=True)
    password = models.CharField(max_length=256)
    name = models.CharField(max_length=50)

    class Mata:
        db_table = 'app_user'
#商品
class Goods(models.Model):
    # 商品ID
    productid = models.CharField(max_length=10)
    # 商品图片
    productimg = models.CharField(max_length=100)
    # 商品名称
    productname = models.CharField(max_length=100)
    # 商品价格
    price = models.DecimalField(max_digits=6,decimal_places=2)
    # 库存
    storenums = models.IntegerField()
    # 销售
    productnum = models.IntegerField()

    class Meta:
        db_table = 'app_goods'