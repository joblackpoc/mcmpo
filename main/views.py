from django.shortcuts import render, redirect
from . models import Header, About
from . forms import AboutForm
# Create your views here.
def index(request):
    header = Header.objects.all()
    return render(request, 'home.html', {'header': header})

def about(request):
    about = About.objects.all()
    return render(request, 'about.html', {'about': about})

def about_add(request):
    if request.method == 'POST':
        form = AboutForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('about')
    else:
        form = AboutForm()
    return render(request, 'about_add.html', {'form' : form})
    

def service(request):
    return render(request, 'service.html')