from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import CustomerForm
from django.contrib import messages


# Create your views here.

def home_greetings(request):

    greetings = ['Hello!!', 'Wilkommen', 'مرحباً', 'স্বাগতম']
    return render(request, 'home.html', {'greetings': greetings})



def about_me(request):
    return render(request, 'about_me.html')

def contact(request):
    done = False

    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            done = True
            return render(request, 'contact.html', {'form': CustomerForm(), 'done': done})

    form = CustomerForm()
    done=False
    context = {'form': form, 'done': done}
    return render(request, 'contact.html', context)


def projects(request):
    return render(request,'projects.html')