# -*- coding: utf-8 -*-
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.conf import settings
from django.shortcuts import render, render_to_response, get_object_or_404, redirect
from django.http import HttpResponseRedirect, Http404
from django.db.models import Sum, Avg, Count, Min, Max
from .forms import KlubForm, PostForm, ClubForm
from .models import Klub, Zawodnik, Trener, Mecz, Info_mecz, Stadion, Post, Clubs

# Create your views here.
def home(request):


	def get_objs(var, stadion_number, aggregate_func):
		z = Mecz.objects.filter(stadion_nr=stadion_number).aggregate(aggregate_func(var))
		return z

	def get_nazwa(nazwa):
		z = Klub.objects.filter(Nazwa=nazwa)
		return z


	context = { 
	"pogon":get_objs('widownia',2,aggregate_func=Avg),
	"pogon_max":get_objs('widownia',2,aggregate_func=Max),
	"pogon_min":get_objs('widownia',2,aggregate_func=Min),
	"pogon_sum":get_objs('widownia',2,aggregate_func=Sum),

	"legia":get_objs('widownia',1,aggregate_func=Avg),
	"legia_max":get_objs('widownia',1,aggregate_func=Max),
	"legia_min":get_objs('widownia',1,aggregate_func=Min),
	"legia_sum":get_objs('widownia',1,aggregate_func=Sum),

	"lech":get_objs('widownia',5,aggregate_func=Avg),
	"lech_max":get_objs('widownia',5,aggregate_func=Max),
	"lech_min":get_objs('widownia',5,aggregate_func=Min),
	"lech_sum":get_objs('widownia',5,aggregate_func=Sum),

	"lechia":get_objs('widownia',8,aggregate_func=Avg),
	"lechia_max":get_objs('widownia',8,aggregate_func=Max),
	"lechia_min":get_objs('widownia',8,aggregate_func=Min),
	"lechia_sum":get_objs('widownia',8,aggregate_func=Sum),


	"klub_pogon":get_nazwa(nazwa='Pogon Szczecin'),
	"klub_legia":get_nazwa(nazwa='Legia Warszawa'),
	"klub_lech":get_nazwa(nazwa='Lech Poznań'),
	"klub_lechia":get_nazwa(nazwa='Lechia Gdańsk'),

	}


	return render(request, "home.html", context)



def tabela_strzelcow(request):
	#queryset = Mecz.objects.order_by('-widownia')


	infos = Zawodnik.objects.order_by('-id')


	context = { 
	"infos":infos
	}


	return render(request, "tabela_strzelcow.html", context)

def druzyny(request):


	return render(request, "druzyny.html")




def tabela(request):

	form = KlubForm(request.POST or None)
	if request.user.is_authenticated():


		if form.is_valid():
			instance = form.save(commit=False)

			Nazwa = form.cleaned_data.get("Nazwa")
			if not instance.Nazwa:
				Nazwa = ""

			instance.Nazwa = Nazwa
			instance.save()



	queryset = Clubs.objects.order_by('-punkty')
	ziomset = Zawodnik.objects.order_by('-klub')



	Clubs.objects.distinct()
	Zawodnik.objects.distinct()

	context = { 
	"queryset":queryset,
	"ziomset":ziomset,
	"form":form,
	}
	return render(request, "tabela.html", context,)


def pogon(request):

	goles = Info_mecz.objects.filter(nr_zawodnika=1).aggregate(Sum('gole_zawodnika'))
	gole = Info_mecz.objects.select_related("nr_zawodnika")
	queryset = Klub.objects.filter(Nazwa='Pogon Szczecin')
	stadion = Stadion.objects.filter(klub=1)
	trener = Trener.objects.filter(klub=1)
	ziomset = Zawodnik.objects.filter(klub=1).order_by('-pozycja','nr_zawodnika')
		#Entry.objects.order_by(Coalesce('summary', 'headline').desc())
	#gole = Info_mecz.objects.values('gole_zawodnika')
	context = { 
	"queryset":queryset,
	"ziomset":ziomset,
	"gole":gole,
	"goles":goles,
	"stadion":stadion,
	"trener":trener
	}
	return render(request, "pogon.html", context,)

# blog/post

def post_list(request):
	#if request.user.is_authenticated():
		#istance = get_object_or_404(Post, id=1)
	queryset_list = Post.objects.all()#.order_by("-timestamp")
	paginator = Paginator(queryset_list, 5) # Show 5 queryset per page
	page_request_var = 'page'


	page = request.GET.get('page')
	try:
		queryset = paginator.page(page)
	except PageNotAnInteger:
		# If page is not an integer, deliver first page.
		queryset = paginator.page(1)
	except EmptyPage:
		# If page is out of range (e.g. 9999), deliver last page of results.
		queryset = paginator.page(paginator.num_pages)
	context = {
		
		"object_list":queryset,
		"page_request_var":page_request_var

	}

	return render(request, "post_list.html", context)




def post_create(request):
	if not request.user.is_staff or not request.user.is_superuser:
		raise Http404


	#if not request.user.is_authenticated():
	#	raise Http404


	form = PostForm(request.POST or None, request.FILES or None)
	if form.is_valid():

		instance = form.save(commit=False)
		instance.user = request.user
		instance.save()
		messages.success(request, "Sukces w stworzeniu")

#	if request.method == "POST":
#		title = request.POST.get("title")
#		#Post.objects.create(title=title)
	else:
		messages.error(request, "blad w stworzeniu")
	context = {
	"form":form,
	}

	return render(request, "post_form.html", context,)

def post_detail(request, id=None):

	#if request.user.is_authenticated():

	instance = get_object_or_404(Post, id=id)

	context = {
		"title":instance.title,
		"instance":instance,
	}

	return render(request, "post_detail.html", context,)

def post_update(request, id=None):
	if not request.user.is_staff or not request.user.is_superuser:
		raise Http404
	instance = get_object_or_404(Post, id=id)
	form = PostForm(request.POST or None, request.FILES or None, instance=instance )
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		messages.success(request, "Sukces w zapisaniu")
	else:
		messages.error(request, "blad w zapisaniu")

	context = {
			"title":instance.title,
			"instance":instance,
			"form":form,
		}


	return render(request, "post_form.html", context,)

	

def post_delete(request, id=None):
	if not request.user.is_staff or not request.user.is_superuser:
		raise Http404
	instance = get_object_or_404(Post, id=id)
	if request.method == "POST":
		instance.delete()
		return redirect('/')
	context = {
			"instance":instance,
		}
	return render(request, "delete.html", context)




def club_create(request):
	if not request.user.is_staff or not request.user.is_superuser:
		raise Http404

	form = ClubForm(request.POST or None, request.FILES or None)
	if form.is_valid():

		instance = form.save(commit=False)
		instance.user = request.user
		instance.save()
		messages.success(request, "Sukces w stworzeniu")

#	if request.method == "POST":
#		title = request.POST.get("title")
#		#Post.objects.create(title=title)
	else:
		messages.error(request, "blad w stworzeniu")
	context = {
	"form":form,
	}

	return render(request, "club_form.html", context,)

def club_detail(request, id=None):

	#if request.user.is_authenticated():

	instance = get_object_or_404(Clubs, id=id)
	ziomset = Zawodnik.objects.filter(klubs_id=id).order_by('-pozycja','-nr_zawodnika')

	context = {
		"nazwa":instance.nazwa,
		"instance":instance,
		"ziomset":ziomset
	}

	return render(request, "club_detail.html", context,)