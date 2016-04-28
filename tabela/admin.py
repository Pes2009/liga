# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin

from .models import Klub, Zawodnik, Trener, Mecz, Info_mecz, Stadion



class ZawodnikInline(admin.TabularInline):



    model = Zawodnik
    extra = 3


class KlubAdmin(admin.ModelAdmin):


	fieldsets = [
	(None,               {'fields': ['Nazwa']}),
	('Dane szczegolowe', {'fields': ['punkty','zwyciestwa','remisy','porazki'], 'classes': ['collapse']}),
	]
	inlines = [ZawodnikInline]


class TrenerAdmin(admin.ModelAdmin):

    model = Trener

class MeczAdmin(admin.ModelAdmin):

    model = Mecz

class Info_meczAdmin(admin.ModelAdmin):

    model = Info_mecz


class StadionAdmin(admin.ModelAdmin):

    model = Stadion



admin.site.register(Klub, KlubAdmin)
admin.site.register(Zawodnik)
admin.site.register(Trener, TrenerAdmin)
admin.site.register(Mecz, MeczAdmin)
admin.site.register(Info_mecz, Info_meczAdmin)
admin.site.register(Stadion, StadionAdmin)