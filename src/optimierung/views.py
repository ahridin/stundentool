from django.shortcuts import render
from .datencheck import datenpruefer
from .main_skript import doeverything
from django.contrib.auth.decorators import login_required

from django.http import HttpResponseRedirect
from .forms import ParameterForm

# Create your views here.
@login_required
def optimierung_main(request):
    return render(request, 'optimierung/optimierung_main.html',)

@login_required
def datencheck(request):
    print("datencheck")
    messages = datenpruefer.machdencheck(datenpruefer)
    if messages == []:
        messages = ["Ihre Daten haben den Datencheck bestanden. Gehen sie nun weiter zum nächsten Schritt"]

    return render(request, 'optimierung/datencheck.html', {'messages': messages})

@login_required
def parameters(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ParameterForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            ''' parameter verarbeiten
            '''
            form.save()
            # redirect to a new URL:
            #return HttpResponseRedirect('/thanks/')
    # if a GET (or any other method) we'll create a blank form
    else:
        form = ParameterForm()

    return render(request, 'optimierung/parameters.html', {'form': form})


@login_required
def optimierung(request):
    done = doeverything()
    return render(request, 'optimierung/optimierung.html', {'done': done})
