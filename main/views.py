from django.shortcuts import render
from django.shortcuts import render_to_response, get_object_or_404
from main.models import *
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

def festival(request,id):
    festival = get_object_or_404(Festival, alias=id)
    context = {'festival': festival }
    return render_to_response('festival.html', context)
