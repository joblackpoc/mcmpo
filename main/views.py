from django.shortcuts import render
from .models import Header
# Create your views here.
def index(request):
    header = Header.objects.all()
    return render(request, 'home.html', {'header': header})

def about(request):
    return render(request, 'about.html')

def service(request):
    return render(request, 'service.html')