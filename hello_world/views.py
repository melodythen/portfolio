from django.shortcuts import render

# Create your views here.

def hello_world(request):
    return render(request, 'hello_world.html', {}) 


def test(request):
    return render(request,'test.html',{})


def resume(request):
    return render(request,'resume.html',{})