from django.contrib import admin

from rbac import models


class PermissionConf(admin.ModelAdmin):
    list_display = ['id', 'url', 'title']
    list_editable = ['url', 'title']


admin.site.register(models.Permission, PermissionConf)
admin.site.register(models.Role)
admin.site.register(models.User)
