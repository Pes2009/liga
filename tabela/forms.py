# -*- coding: utf-8 -*-
from django import forms
from .models import Klub
from django.contrib.auth.models import User


class KlubForm(forms.ModelForm):
	class Meta:
		model = Klub
		fields = ['Nazwa', 'punkty','zwyciestwa','remisy','porazki']


	def clean_full_name(self):
		Nazwa  = self.cleaned_data.get('Nazwa')

		return Nazwa

