from django.contrib import admin

from rbac import models


class PermissionConf(admin.ModelAdmin):
    list_display = ['id', 'url', 'title', 'menu']
    list_editable = ['url', 'title', 'menu']


admin.site.register(models.Permission, PermissionConf)
admin.site.register(models.Role)
admin.site.register(models.User)
admin.site.register(models.Menu)
