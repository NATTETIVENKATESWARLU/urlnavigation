from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'index.html')

def HELLO(request):
    return render(request,'hello.html')
