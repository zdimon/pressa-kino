# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.shortcuts import render_to_response, get_object_or_404
from main.models import *
from django.views.generic import ListView, DetailView
import datetime
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from main.models import Vote
from django.forms import ModelForm, HiddenInput
from django.shortcuts import render
from django.contrib import messages
import json
import os
import uuid
from kino.settings import VIDEO_DIR, LINK_DIR
from multiprocessing import Pool
import time

def delayselete(hash):
    time.sleep(4)
    print 'deleting'
    dst = LINK_DIR+'/'+hash+'.mp4'
    os.remove(dst)


def showme(request,id):
    pool = Pool(processes=1)
    film = get_object_or_404(Film, pk=id)
    hash = str(uuid.uuid4())
    src = VIDEO_DIR+'/'+film.ftp
    dst = LINK_DIR+'/'+hash+'.mp4'
    os.symlink(src, dst)
    result = pool.apply_async(delayselete, [hash])
    data = {'status': 0, 'id': film.id, 'hash': hash}

    return HttpResponse(json.dumps(data), mimetype='application/json')

class MessageForm(ModelForm):
    class Meta:
        model = Message
        fields = ['name', 'text', 'film']
        widgets = {'film': HiddenInput()}


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

def festival(request,id,catalog):
    festival = get_object_or_404(Festival, alias=id)
    catalogs = festival.get_catalogs()
    try:
        catalog = Catalog.objects.get(pk=catalog)
    except:
        catalog = None
        

    if (festival.is_in_catalog and catalog==None):
         hide = True
    else:
         hide = False

    #print catalogs
    #if (festival.is_in_catalog):
    #    tpl = 'catalog.html'
    #else:
    
    tpl = 'festival.html'
    if catalog:
        films = Film.objects.filter(festival=festival, catalog=catalog).order_by('-release_date')
        curc = catalog.id
    else:
        films = Film.objects.filter(festival=festival).order_by('-release_date')
        curc = 0



   		
    context = {'festival': festival, 'films': films, 'catalogs': catalogs, 'curc': curc, 'hide': hide}
    return render_to_response(tpl, context)


def film(request,id):
    film = get_object_or_404(Film, id=id)
    mess = Message.objects.filter(film=film, is_published=True)
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Спасибо. Ваше сообщение сохранено и появится после проверки Администрацией.")
            # do something.
    else:
        mes = Message()
        mes.film = film
        form = MessageForm(instance=mes)
    context = {'film': film, 'form': form, 'mess': mess }
    return render(request,'film.html', context)



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
    
    