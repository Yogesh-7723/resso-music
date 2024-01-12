from django.shortcuts import render,redirect
from .models import *
from django.http import HttpResponse
from django.contrib import messages
from django.core.exceptions import ValidationError
# Create your views here.

def index(request):
    songs = AddSong.objects.all()
    return render(request,"index.html",{'songs':songs})

def delete(request,uid):
    AddSong.objects.get(id=uid).delete()
    return redirect('/')

def createsong(request):
    return render(request,'songs.html')

def newsong(request):
    if request.method == 'POST':
        s_name = request.POST['s_name']
        artist = request.POST['artist']
        detail = request.POST['detail']
        song =   request.FILES['song']
        if AddSong.objects.filter(song=song).exists():
            return HttpResponse("Song Already Available")
        else:
            AddSong.objects.create(s_name=s_name,artist=artist,
                            detail=detail,song=song)
            return redirect('/')
            
            
def update(request,qk):
    obj = AddSong.objects.get(id=qk)
    return render(request,'update.html',{'obj':obj})


def updateview(request):
    if request.method == 'POST':
        s_name = request.POST['s_name']
        artist = request.POST['artist']
        detail = request.POST['detail']
        song = request.FILES['song']
        if AddSong.objects.filter(song=song).exists():
            return HttpResponse("Song Already Available")
        else:
            AddSong.objects.create(s_name=s_name,artist=artist,
                            detail=detail,song=song)
            return redirect('/')