from django.shortcuts import render

# Create your views here.

def A(request):
    return render(request,'a.html')

def B(request):
    return render(request,'b.html')
