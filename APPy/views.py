from django.shortcuts import render
from .models import Dht
# Create your views here.
from django.http import HttpResponse
def home(request):
  return HttpResponse('bonj à tous')




def charts(request):
  tab = Dht.objects.all()
  s = {'tab': tab}
  return render(request, 'charts.html', s)


def table(request):
  tab = Dht.objects.all()
  s = {'tab': tab}
  return render(request, 'table.html', s)


def tables(request):
  tab = Dht.objects.all()
  x = {'tab': tab}
  return render(request, 'table.html', x)