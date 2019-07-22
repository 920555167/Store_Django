from django.db import models

class Seller(models.Model):
    username=models.CharField(max_length=32,verbose_name='用户名')
    password=models.CharField(max_length=32,verbose_name='密码')
    Nickname=models.CharField(max_length=32,verbose_name='昵称')
    Phone=models.CharField(max_length=32,verbose_name='电话')
    Email=models.CharField(max_length=32,verbose_name='邮箱')
    Picture=models.CharField(max_length=32,verbose_name='头像')
    Address=models.CharField(max_length=32,verbose_name='地址')
    card_id=models.CharField(max_length=32,verbose_name='身份证')
class StoreType(models.Model):
     store_type=models.CharField(max_length=32,verbose_name='类型名称')
     type_descripton=models.TextField(verbose_name='类型名称')
class Store(models.Model):
    store_name=models.CharField(max_length=32,verbose_name='店铺名')
    s