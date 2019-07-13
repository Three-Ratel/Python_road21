from django.contrib import admin

from rbac import models


class PermissionConf(admin.ModelAdmin):
    list_display = ['id', 'url', 'title', 'icon', 'is_menu']
    list_editable = ['url', 'title', 'icon', 'is_menu']


admin.site.register(models.Permission, PermissionConf)
admin.site.register(models.Role)
admin.site.register(models.User)
