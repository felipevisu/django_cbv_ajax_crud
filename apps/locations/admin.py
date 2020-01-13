from django.contrib import admin

from .models import *

class SectorInline(admin.StackedInline):
    model = Sector
    extra = 0


class NeighborhoodInline(admin.StackedInline):
    model = Neighborhood
    extra = 0


class SectorAdmin(admin.ModelAdmin):
    inlines = [NeighborhoodInline]


class CityAdmin(admin.ModelAdmin):
    inlines = [SectorInline]


admin.site.register(Sector, SectorAdmin)
admin.site.register(City, CityAdmin)
