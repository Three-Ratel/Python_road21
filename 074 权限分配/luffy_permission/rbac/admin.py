from django.contrib import admin

from rbac import models


class PermissionConf(admin.ModelAdmin):
    list_display = ['id', 'url', 'title', 'menu']
    list_editable = ['url', 'title', 'menu']


class MenuConf(admin.ModelAdmin):
    list_display = ['id', 'title', 'icon', 'weight']
    list_editable = ['title', 'weight', 'icon']


admin.site.register(models.Permission, PermissionConf)
admin.site.register(models.Role)
admin.site.register(models.User)
admin.site.register(models.Menu, MenuConf)
