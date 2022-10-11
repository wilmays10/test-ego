from django.contrib import admin

from car.models import Brand, Group, Version, Price


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Brand._meta.fields]
    search_fields = ['name']

@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Group._meta.fields]
    search_fields = ['name']
    list_filter = ['brand__name']

@admin.register(Version)
class VersionAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Version._meta.fields]
    search_fields = ['name']
    list_filter = ['group__name', 'group__brand__name']

@admin.register(Price)
class PriceAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Price._meta.fields]
    list_filter = ['year', 'version__name', 'version__group__name',
                   'version__group__brand__name']
