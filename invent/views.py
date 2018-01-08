from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView # Import TemplateView

from .forms import NameForm
 

def index(request):
    return HttpResponse('hello from invent')

def about(request):
    return render(request, 'test.html',{'nazwa':'dupa'})
def get_name(request):
    if request.method == 'POST':
        form = NameForm(request.POST)
        if form.is_valid():
            print (form.cleaned_data['your_name'])
        else:
            print ('invalid :(')

    else:
        form = NameForm()
    return render(request, 'form.html', {'form':form, 'handler': 'your_name'})
