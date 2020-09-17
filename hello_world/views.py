from django.shortcuts import render, redirect
from django.views.generic import View


def hello_world(request):
    return render(request, 'hello_world.html', {}) 


def test(request):
    return render(request,'test.html',{})


def resume(request):
    return render(request,'resume.html',{})


