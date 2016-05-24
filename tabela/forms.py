# -*- coding: utf-8 -*-
from django import forms
from .models import Klub, Post
from django.contrib.auth.models import User
from django.utils.translation import ugettext
from django.utils.translation import ugettext_lazy as _


class KlubForm(forms.ModelForm):
	class Meta:
		model = Klub
		fields = ['Nazwa','data_powstania', 'punkty','zwyciestwa','remisy','porazki']


	def clean_full_name(self):
		Nazwa  = self.cleaned_data.get('Nazwa')

		return Nazwa

class PostForm(forms.ModelForm):
	class Meta:
		model = Post

		fields = [
			"title",
			"content",
			"image",
			"draft",
			"publish",
		]

