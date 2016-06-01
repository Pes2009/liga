# -*- coding: utf-8 -*-
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.conf import settings
from django.shortcuts import render, render_to_response, get_object_or_404, redirect
from django.http import HttpResponseRedirect, Http404
from django.db.models import Sum, Avg, Count, Min, Max
from .forms import KlubForm, PostForm
from .models import Klub, Zawodnik, Trener, Mecz, Info_mecz, Stadion, Post, Project, Cost


def homes(request):



	return render(request, "canvas.html")


# Create your views here.
def home(request):

	queryset = Mecz.objects.order_by('-widownia')
	pogon = Mecz.objects.filter(stadion_nr=2).aggregate(Avg('widownia'))
	pogon_max = Mecz.objects.filter(stadion_nr=2).aggregate(Max('widownia'))
	pogon_min = Mecz.objects.filter(stadion_nr=2).aggregate(Min('widownia'))
	pogon_sum = Mecz.objects.filter(stadion_nr=2).aggregate(Sum('widownia'))

	legia = Mecz.objects.filter(stadion_nr=1).aggregate(Avg('widownia'))
	legia_max = Mecz.objects.filter(stadion_nr=1).aggregate(Max('widownia'))
	legia_min = Mecz.objects.filter(stadion_nr=1).aggregate(Min('widownia'))
	legia_sum = Mecz.objects.filter(stadion_nr=1).aggregate(Sum('widownia'))

	lech = Mecz.objects.filter(stadion_nr=5).aggregate(Avg('widownia'))
	lech_max = Mecz.objects.filter(stadion_nr=5).aggregate(Max('widownia'))
	lech_min = Mecz.objects.filter(stadion_nr=5).aggregate(Min('widownia'))
	lech_sum = Mecz.objects.filter(stadion_nr=5).aggregate(Sum('widownia'))

	lechia = Mecz.objects.filter(stadion_nr=8).aggregate(Avg('widownia'))
	lechia_max = Mecz.objects.filter(stadion_nr=8).aggregate(Max('widownia'))
	lechia_min = Mecz.objects.filter(stadion_nr=8).aggregate(Min('widownia'))
	lechia_sum = Mecz.objects.filter(stadion_nr=8).aggregate(Sum('widownia'))


	klub_pogon = Klub.objects.filter(Nazwa='Pogon Szczecin')
	klub_legia = Klub.objects.filter(Nazwa='Legia Warszawa')
	klub_lech = Klub.objects.filter(Nazwa='Lech Poznań')
	klub_lechia = Klub.objects.filter(Nazwa='Lechia Gdańsk')



	context = { 
	"pogon":pogon,
	"pogon_max":pogon_max,
	"pogon_min":pogon_min,
	"pogon_sum":pogon_sum,

	"legia":legia,
	"legia_max":legia_max,
	"legia_min":legia_min,
	"legia_sum":legia_sum,

	"lech":lech,
	"lech_max":lech_max,
	"lech_min":lech_min,
	"lech_sum":lech_sum,

	"lechia":lechia,
	"lechia_max":lechia_max,
	"lechia_min":lechia_min,
	"lechia_sum":lechia_sum,


	"queryset":queryset,
	"klub_pogon":klub_pogon,
	"klub_legia":klub_legia,
	"klub_lech":klub_lech,
	"klub_lechia":klub_lechia

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



	queryset = Klub.objects.order_by('-punkty')
	ziomset = Zawodnik.objects.order_by('-klub')



	Klub.objects.distinct()
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



def legia(request):

	gole = Info_mecz.objects.all().aggregate(Avg('gole_zawodnika'))
	queryset = Klub.objects.filter(Nazwa='Legia Warszawa')
	stadion = Stadion.objects.filter(klub=2)
	trener = Trener.objects.filter(klub=2)
	ziomset = Zawodnik.objects.filter(klub=2).order_by('-pozycja','-nr_zawodnika')
		#Entry.objects.order_by(Coalesce('summary', 'headline').desc())
	#gole = Info_mecz.objects.values('gole_zawodnika')

	context = { 
	"queryset":queryset,
	"ziomset":ziomset,
	"gole":gole,
	"stadion":stadion,
	"trener":trener
	}
	return render(request, "legia.html", context,)


def lech(request):

	gole = Info_mecz.objects.all().aggregate(Avg('gole_zawodnika'))
	queryset = Klub.objects.filter(Nazwa='Lech Poznań')
	stadion = Stadion.objects.filter(klub=3)
	trener = Trener.objects.filter(klub=3)
	ziomset = Zawodnik.objects.filter(klub=3).order_by('-pozycja','-nr_zawodnika')
		#Entry.objects.order_by(Coalesce('summary', 'headline').desc())
	#gole = Info_mecz.objects.values('gole_zawodnika')

	context = { 
	"queryset":queryset,
	"ziomset":ziomset,
	"gole":gole,
	"stadion":stadion,
	"trener":trener,
	}
	return render(request, "lech.html", context,)


def lechia(request):

	gole = Info_mecz.objects.all().aggregate(Avg('gole_zawodnika'))
	queryset = Klub.objects.filter(Nazwa='Lechia Gdańsk')
	stadion = Stadion.objects.filter(klub=4)
	trener = Trener.objects.filter(klub=4)
	ziomset = Zawodnik.objects.filter(klub=4).order_by('-pozycja','-nr_zawodnika')
		#Entry.objects.order_by(Coalesce('summary', 'headline').desc())
	#gole = Info_mecz.objects.values('gole_zawodnika')

	context = { 
	"queryset":queryset,
	"ziomset":ziomset,
	"gole":gole,
	"stadion":stadion,
	"trener":trener
	}
	return render(request, "lechia.html", context,)

def slask(request):

	gole = Info_mecz.objects.all().aggregate(Avg('gole_zawodnika'))
	queryset = Klub.objects.filter(Nazwa='Śląsk Wroclaw')
	stadion = Stadion.objects.filter(klub=5)
	trener = Trener.objects.filter(klub=5)
	ziomset = Zawodnik.objects.filter(klub=5).order_by('-pozycja','-nr_zawodnika')
		#Entry.objects.order_by(Coalesce('summary', 'headline').desc())
	#gole = Info_mecz.objects.values('gole_zawodnika')

	context = { 
	"queryset":queryset,
	"ziomset":ziomset,
	"gole":gole,
	"stadion":stadion,
	"trener":trener
	}
	return render(request, "slask.html", context,)


def jagiellonia(request):

	gole = Info_mecz.objects.all().aggregate(Avg('gole_zawodnika'))
	queryset = Klub.objects.filter(Nazwa='Jagiellonia Białystok')
	stadion = Stadion.objects.filter(klub=6)
	trener = Trener.objects.filter(klub=6)
	ziomset = Zawodnik.objects.filter(klub=6).order_by('-pozycja','-nr_zawodnika')
		#Entry.objects.order_by(Coalesce('summary', 'headline').desc())
	#gole = Info_mecz.objects.values('gole_zawodnika')

	context = { 
	"queryset":queryset,
	"ziomset":ziomset,
	"gole":gole,
	"stadion":stadion,
	"trener":trener
	}
	return render(request, "Jagiellonia.html", context,)

def wisla(request):

	gole = Info_mecz.objects.all().aggregate(Avg('gole_zawodnika'))
	queryset = Klub.objects.filter(Nazwa='Wisła Kraków')
	stadion = Stadion.objects.filter(klub=7)
	trener = Trener.objects.filter(klub=7)
	ziomset = Zawodnik.objects.filter(klub=7).order_by('-pozycja','-nr_zawodnika')
		#Entry.objects.order_by(Coalesce('summary', 'headline').desc())
	#gole = Info_mecz.objects.values('gole_zawodnika')

	context = { 
	"queryset":queryset,
	"ziomset":ziomset,
	"gole":gole,
	"stadion":stadion,
	"trener":trener
	}
	return render(request, "wisla.html", context,)


def cracovia(request):

	gole = Info_mecz.objects.all().aggregate(Avg('gole_zawodnika'))
	queryset = Klub.objects.filter(Nazwa='Cracovia Kraków')
	stadion = Stadion.objects.filter(klub=8)
	trener = Trener.objects.filter(klub=8)
	ziomset = Zawodnik.objects.filter(klub=8).order_by('-pozycja','-nr_zawodnika')
		#Entry.objects.order_by(Coalesce('summary', 'headline').desc())
	#gole = Info_mecz.objects.values('gole_zawodnika')

	context = { 
	"queryset":queryset,
	"ziomset":ziomset,
	"gole":gole,
	"stadion":stadion,
	"trener":trener
	}
	return render(request, "cracovia.html", context,)

def gornik_zabrze(request):

	gole = Info_mecz.objects.all().aggregate(Avg('gole_zawodnika'))
	queryset = Klub.objects.filter(Nazwa='Górnik Zabrze')
	stadion = Stadion.objects.filter(klub=9)
	trener = Trener.objects.filter(klub=9)
	ziomset = Zawodnik.objects.filter(klub=9).order_by('-pozycja','-nr_zawodnika')
		#Entry.objects.order_by(Coalesce('summary', 'headline').desc())
	#gole = Info_mecz.objects.values('gole_zawodnika')

	context = { 
	"queryset":queryset,
	"ziomset":ziomset,
	"gole":gole,
	"stadion":stadion,
	"trener":trener
	}
	return render(request, "gornik_zabrze.html", context,)

def gornik_leczna(request):

	gole = Info_mecz.objects.all().aggregate(Avg('gole_zawodnika'))
	queryset = Klub.objects.filter(Nazwa='Górnik Łęczna')
	stadion = Stadion.objects.filter(klub=10)
	trener = Trener.objects.filter(klub=10)
	ziomset = Zawodnik.objects.filter(klub=10).order_by('-pozycja','-nr_zawodnika')
		#Entry.objects.order_by(Coalesce('summary', 'headline').desc())
	#gole = Info_mecz.objects.values('gole_zawodnika')

	context = { 
	"queryset":queryset,
	"ziomset":ziomset,
	"gole":gole,
	"stadion":stadion,
	"trener":trener
	}
	return render(request, "gornik_leczna.html", context,)



def podbeskidzie(request):

	gole = Info_mecz.objects.all().aggregate(Avg('gole_zawodnika'))
	queryset = Klub.objects.filter(Nazwa='Podbeskidzie Bielsko-Biała')
	stadion = Stadion.objects.filter(klub=11)
	trener = Trener.objects.filter(klub=11)
	ziomset = Zawodnik.objects.filter(klub=11).order_by('-pozycja','-nr_zawodnika')
		#Entry.objects.order_by(Coalesce('summary', 'headline').desc())
	#gole = Info_mecz.objects.values('gole_zawodnika')

	context = { 
	"queryset":queryset,
	"ziomset":ziomset,
	"gole":gole,
	"stadion":stadion,
	"trener":trener
	}
	return render(request, "podbeskidzie.html", context,)



def zaglebie(request):

	gole = Info_mecz.objects.all().aggregate(Avg('gole_zawodnika'))
	queryset = Klub.objects.filter(Nazwa='Zagłebie Lubin')
	stadion = Stadion.objects.filter(klub=12)
	trener = Trener.objects.filter(klub=12)
	ziomset = Zawodnik.objects.filter(klub=12).order_by('-pozycja','-nr_zawodnika')
		#Entry.objects.order_by(Coalesce('summary', 'headline').desc())
	#gole = Info_mecz.objects.values('gole_zawodnika')

	context = { 
	"queryset":queryset,
	"ziomset":ziomset,
	"gole":gole,
	"stadion":stadion,
	"trener":trener
	}
	return render(request, "zaglebie.html", context,)

def piast(request):

	gole = Info_mecz.objects.all().aggregate(Avg('gole_zawodnika'))
	queryset = Klub.objects.filter(Nazwa='Piast Gliwice')
	stadion = Stadion.objects.filter(klub=13)
	trener = Trener.objects.filter(klub=13)
	ziomset = Zawodnik.objects.filter(klub=13).order_by('-pozycja','-nr_zawodnika')
		#Entry.objects.order_by(Coalesce('summary', 'headline').desc())
	#gole = Info_mecz.objects.values('gole_zawodnika')

	context = { 
	"queryset":queryset,
	"ziomset":ziomset,
	"gole":gole,
	"stadion":stadion,
	"trener":trener
	}
	return render(request, "piast.html", context,)



def ruch(request):

	gole = Info_mecz.objects.all().aggregate(Avg('gole_zawodnika'))
	queryset = Klub.objects.filter(Nazwa='Ruch Chorzów')
	stadion = Stadion.objects.filter(klub=14)
	trener = Trener.objects.filter(klub=14)
	ziomset = Zawodnik.objects.filter(klub=14).order_by('-pozycja','-nr_zawodnika')
		#Entry.objects.order_by(Coalesce('summary', 'headline').desc())
	#gole = Info_mecz.objects.values('gole_zawodnika')

	context = { 
	"queryset":queryset,
	"ziomset":ziomset,
	"gole":gole,
	"stadion":stadion,
	"trener":trener
	}
	return render(request, "ruch.html", context,)

def termalika(request):

	gole = Info_mecz.objects.all().aggregate(Avg('gole_zawodnika'))
	queryset = Klub.objects.filter(Nazwa='Termalika Bruk-bet Nieciecza')
	stadion = Stadion.objects.filter(klub=15)
	trener = Trener.objects.filter(klub=15)
	ziomset = Zawodnik.objects.filter(klub=15).order_by('-pozycja','-nr_zawodnika')
		#Entry.objects.order_by(Coalesce('summary', 'headline').desc())
	#gole = Info_mecz.objects.values('gole_zawodnika')

	context = { 
	"queryset":queryset,
	"ziomset":ziomset,
	"gole":gole,
	"stadion":stadion,
	"trener":trener
	}
	return render(request, "termalika.html", context,)


def korona(request):

	gole = Info_mecz.objects.all().aggregate(Avg('gole_zawodnika'))
	queryset = Klub.objects.filter(Nazwa='Korona Kielce')
	stadion = Stadion.objects.filter(klub=16)
	trener = Trener.objects.filter(klub=16)
	ziomset = Zawodnik.objects.filter(klub=16).order_by('-pozycja','-nr_zawodnika')
		#Entry.objects.order_by(Coalesce('summary', 'headline').desc())
	#gole = Info_mecz.objects.values('gole_zawodnika')

	context = { 
	"queryset":queryset,
	"ziomset":ziomset,
	"gole":gole,
	"stadion":stadion,
	"trener":trener
	}
	return render(request, "korona.html", context,)



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
