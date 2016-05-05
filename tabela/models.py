# -*- coding: utf-8 -*-
from django.conf import settings
from django.db import models
import datetime
from django.db.models.signals import pre_save
from django.core.urlresolvers import reverse
from django.utils.text import slugify

class Klub(models.Model):
	Nazwa = models.CharField(max_length=50, blank=False, null=False, unique=True)
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False,)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True,)
	punkty = models.IntegerField(blank=False,null=True,)
	porazki = models.IntegerField(blank=False,null=True,)
	zwyciestwa = models.IntegerField(blank=False,null=True,)
	remisy = models.IntegerField(blank=False,null=True,)

	def __unicode__(self):             
		return self.Nazwa


class Stadion(models.Model):
	nazwa = models.CharField(max_length=50, blank=False, null=False, unique=True)
	miasto = models.CharField(max_length=50,blank=False,null=False,)
	ulica = models.CharField(max_length=50,blank=False,null=False,)
	pojemnosc = models.IntegerField(blank=False,null=False,)
	klub = models.ForeignKey(Klub)


	def __unicode__(self):             
		return self.nazwa


class Zawodnik(models.Model):
	
	nr_zawodnika = models.IntegerField(blank=False, null=False, unique=False)
	imie = models.CharField(max_length=50, blank=False, null=False,)
	nazwisko = models.CharField(max_length=50, blank=False, null=False,)
	pozycja = models.CharField(max_length=50, blank=False, null=True,)
	data_urodzenia = models.DateField(auto_now=False, auto_now_add=False,)
	klub = models.ForeignKey(Klub)


	def __unicode__(self):
		zwroc = ("klub : " + str(self.klub) +"\n imie  " + self.imie +" nazwisko  " + self.nazwisko) 
		return zwroc

class Trener(models.Model):
	klub = models.ForeignKey(Klub)
	imie = models.CharField(max_length=50, blank=False, null=False,)
	nazwisko = models.CharField(max_length=50, blank=False, null=False,)
	data_urodzenia = models.DateField(auto_now=False, auto_now_add=False,)


	def __unicode__(self):           
		return self.imie.encode('ascii', errors='replace')


class Mecz(models.Model):
	data = models.DateField(auto_now_add=True, auto_now=False,)
	godz_spotkania = models.TimeField(auto_now_add=True, auto_now=False,)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True,)
	nr_kolejki = models.IntegerField(blank=False,null=True,)
	widownia = models.IntegerField(blank=False,null=True,)
	gospodarz = models.ForeignKey(Klub,related_name='mecz_gospodarz')
	gosc = models.ForeignKey(Klub,related_name='mecz_gosc')
	czas_gry = models.TimeField(auto_now_add=True, auto_now=False,)
	gole_gosci = models.IntegerField(blank=False,null=True,)
	gole_gospodarz = models.IntegerField(blank=False,null=True,)
	stadion_nr = models.IntegerField(blank=False,null=False,)

	def __unicode__(self):
		info = (str(self.gospodarz), 'kontra', str(self.gosc))
		return str(info).encode('ascii', errors='replace')

class Info_mecz(models.Model):
	gole_zawodnika = models.IntegerField(blank=False,null=True,)
	zolte_kartki = models.IntegerField(blank=False,null=True,)
	asysty = models.IntegerField(blank=False,null=True,)
	stadion_nr = models.IntegerField(blank=False,null=False,)
	nr_zawodnika = models.ForeignKey(Zawodnik)
	nr_meczu = models.ForeignKey(Mecz)

	def __unicode__(self):          
		return str(self.gole_zawodnika)

def upload_location(instance, filename):
	return "%s/%s" %(instance.id, filename)


class Post(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1)
	title = models.CharField(max_length=50)
	slug = models.SlugField(unique=True)
	image = models.FileField(null=True,blank=True)
	#image = models.ImageField(null=True, blank=True, height_field="height_field",width_field="width_field")
	#height_field = models.IntegerField(default=0)
	#width_field = models.IntegerField(default=0)
	content = models.TextField()
	timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
	updated = models.DateTimeField(auto_now=True, auto_now_add=False)


	def __unicode__(self):          
		return self.title


	class Meta:
		ordering = ["-timestamp", "-updated"]


def create_slug(instance, new_slug=None):
	slug = slugify(instance.title)
	if new_slug is not None:
		slug = new_slug
	qs = Post.objects.filter(slug=slug).order_by("-id")
	exists = qs.exists()
	if exists:
		new_slug = "%s-%s" %(slug, qs.first().id)
		return create_slug(instance, new_slug=new_slug)
	return slug


def pre_save_post_receiver(sender, instance, *args, **kwargs):
	if not instance.slug:
		instance.slug = create_slug(instance)


pre_save.connect(pre_save_post_receiver, sender=Post)