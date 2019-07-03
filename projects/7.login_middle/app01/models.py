# Create your models here.
from django.db import models


# Create your models here.
class Publisher(models.Model):
    pid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=32, unique=True)

class Book(models.Model):
    title = models.CharField(max_length=32)
    pub = models.ForeignKey('Publisher', on_delete=models.CASCADE)


class Author(models.Model):
    name = models.CharField(max_length=32)
    books = models.ManyToManyField('Book')


# #
# # 3. 跟进记录表   progress
# #    pid
# #    progress_customer_id     	===>关联到客户customer表
# #    user_id		 				===>关联到销售user表  哪个销售负责 默认全局可见
# #    contact_time	 #跟进时间
# #    current_status  #当前状态   文本备注类型text 包括跟进方式
#
#
# class Progress(models.Model):
#     pid = models.AutoField(primary_key=True)
#     # 联系时间
#     contact_time = models.DateTimeField(auto_now_add=True)
#     # 客户意向，跟进方式
#     current_status = models.CharField(max_length=32)
#     # 外键，关联客户表
#     progress_customer = models.ForeignKey('Customer', on_delete=models.CASCADE, related_name='progress')
#     # 外键，关联销售
#     user = models.ForeignKey('User', on_delete=models.CASCADE, related_name='progress')


class Test(models.Model):
    name = models.CharField(max_length=32)

