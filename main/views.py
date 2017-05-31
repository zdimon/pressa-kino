# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.shortcuts import render_to_response, get_object_or_404
from main.models import *
from django.views.generic import ListView, DetailView
import datetime
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from main.models import Vote


class NewsListView(ListView):
    model = News

class NewsDetailView(DetailView):
    model = News


# Create your views here.
def index(request):
    page_one = get_object_or_404(Page, alias='first')
    page_two = get_object_or_404(Page, alias='second')
    fo = Festival.objects.get(pk=1)
    ft = Festival.objects.get(pk=2)
    festival_one = Film.objects.filter(festival=fo).order_by('-id')[0:10]
    festival_two = Film.objects.filter(festival=ft).order_by('-id')[0:10]
    blog = Blog.objects.all().order_by('-id')[0:10]
    context = {
                'page_one': page_one,
                'page_two': page_two,
                'festival_one': festival_one,
                'festival_two': festival_two,
                'fo': fo,
                'ft': ft,
                'blog': blog
            }
    return render_to_response('index.html', context)


def page(request,id):
    page = get_object_or_404(Page, alias=id)
    context = {'page': page }
    return render_to_response('page.html', context)

def date_range_generator(from_dt,to_dt):
  while from_dt!=to_dt:
    yield from_dt
    from_dt = from_dt + datetime.timedelta(days=1)
    
def get_weekday(nd):
    if nd == 0:
        return 'Пн'    
    if nd == 1:
        return 'Вт'  
    if nd == 2:
        return 'Ср'  
    if nd == 3:
        return 'Чт'  
    if nd == 4:
        return 'Пт'  
    if nd == 5:
        return 'Сб'  
    if nd == 6:
        return 'Вс'  

def festival(request,id):
    festival = get_object_or_404(Festival, alias=id)
    last_film =  Film.objects.filter(festival=festival).order_by('-release_date')[0]
    now = last_film.release_date
    from_dt = now - datetime.timedelta(days=7)
    to_dt =  now + datetime.timedelta(days=7)
    #date_list = [base - datetime.timedelta(days=x) for x in range(0, 13)]
    #dtl = []
    #for d in date_list:
    #    dtl.append(d.day)
    dtl = []
    for dt in date_range_generator(from_dt,to_dt):
        if dt == now:
            is_active = "active"
        else:
            is_active = ""    
        films = []
        for f in Film.objects.filter(release_date=dt, festival=festival):
            films.append(f)
        dtl.append({
                    "date":dt, 
                    "weekday": get_weekday(dt.weekday()),
                    "is_active": is_active,
                    "films": films
                    })
    #print dtl	    			
    context = {'festival': festival, 'dtl': dtl}
    return render_to_response('festival.html', context)


def film(request,id):
    film = get_object_or_404(Film, id=id)
    context = {'film': film }
    return render_to_response('film.html', context)


def blog(request,id):
    blog = get_object_or_404(Blog, id=id)
    context = {'blog': blog }
    return render_to_response('blog.html', context)


@csrf_exempt
def vote(request):
    print
    try:
        vt = Vote.objects.get(obj=request.POST['id'])
    except:
        vt = Vote()
        vt.obj = request.POST['id']
        vt.cnt = 0
        vt.score = 0
    if( request.POST['voted']!='true'):
        vt.cnt = vt.cnt+1
        vt.score = vt.score + int(request.POST['score'])
        vt.save()
    evg = float(vt.score)/vt.cnt
    out = '%s|%.1f|%s' % (str(vt.cnt),evg,vt.obj)
    return HttpResponse(out)
    
    