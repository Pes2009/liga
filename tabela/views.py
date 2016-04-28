# -*- coding: utf-8 -*-
from django.conf import settings
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.db.models import Sum, Avg
from .forms import KlubForm
from .models import Klub, Zawodnik, Trener, Mecz, Info_mecz, Stadion



# Create your views here.
def home(request):


	return render(request, "home.html")





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
	#setset= = Info_mecz.objects.order_by('-gole_zawodnika')
	setset=Info_mecz.objects.annotate(all_gole=Sum('gole_zawodnika'))


	Klub.objects.distinct()
	Zawodnik.objects.distinct()

	context = { 
	"queryset":queryset,
	"ziomset":ziomset,
	"setset":setset,
	"form":form,
	}
	return render(request, "tabela.html", context,)


def pogon(request):

	gole = Info_mecz.objects.all().aggregate(Avg('gole_zawodnika'))
	queryset = Klub.objects.filter(Nazwa='Pogon Szczecin')
	stadion = Stadion.objects.filter(klub=1)
	trener = Trener.objects.filter(klub=1)
	ziomset = Zawodnik.objects.filter(klub=1).order_by('-pozycja','-nr_zawodnika')
		#Entry.objects.order_by(Coalesce('summary', 'headline').desc())
	#gole = Info_mecz.objects.values('gole_zawodnika')

	context = { 
	"queryset":queryset,
	"ziomset":ziomset,
	"gole":gole,
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
	queryset = Klub.objects.filter(Nazwa='Sląsk Wrocław')
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