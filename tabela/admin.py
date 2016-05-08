#!/usr/bin/env/python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin

from .models import Klub, Zawodnik, Trener, Mecz, Info_mecz, Stadion, Post



class ZawodnikInline(admin.TabularInline):



    model = Zawodnik
    extra = 3


class KlubAdmin(admin.ModelAdmin):


	fieldsets = [
	(None,               {'fields': ['Nazwa', 'data_powstania']}),
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

class PostAdmin(admin.ModelAdmin):
    list_display = ["__unicode__","timestamp","title"]
    list_editable = ["title"]
    list_filter = ["title","timestamp"]
    search_fields = ["title", "content"]
    class meta:
        model = Post



admin.site.register(Klub, KlubAdmin)
admin.site.register(Zawodnik)
admin.site.register(Trener, TrenerAdmin)
admin.site.register(Mecz, MeczAdmin)
admin.site.register(Info_mecz, Info_meczAdmin)
admin.site.register(Stadion, StadionAdmin)
admin.site.register(Post, PostAdmin)