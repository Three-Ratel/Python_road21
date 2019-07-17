from django.db import models


class Menu(models.Model):
    title = models.CharField('标题', max_length=32)
    icon = models.CharField('图标', max_length=100, null=True, blank=True)
    weight = models.IntegerField('优先级', default=1)

    def __str__(self):
        return self.title


class Permission(models.Model):
    url = models.CharField('路径', max_length=100)
    title = models.CharField('标题', max_length=32)
    name = models.CharField('url别名', max_length=32, unique=True)
    weight = models.IntegerField('权重', default=0, null=True)
    menu = models.ForeignKey('Menu', null=True, blank=True)
    parent = models.ForeignKey('self', null=True, blank=True)

    def __str__(self):
        return self.title


class Role(models.Model):
    name = models.CharField('角色', max_length=32)
    permissions = models.ManyToManyField('Permission', verbose_name='权限', blank=True)

    def __str__(self):
        return self.name


class User(models.Model):
    username = models.CharField('用户名', max_length=32)
    password = models.CharField('密码', max_length=32)
    roles = models.ManyToManyField('Role', verbose_name='角色')

    def __str__(self):
        return self.username
