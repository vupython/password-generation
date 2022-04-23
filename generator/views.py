from subprocess import list2cmdline
from django.shortcuts import render
from django.http import HttpResponse
import random

#import generator
# Create your views here.

def home(request):
    return render(request, 'generator/home.html')

def about(request):
    return render(request, 'generator/about.html')

def password(request):
    characters = list('askdlfakakdjafdsjfdiksjfsidsjfweifdscx40934349ADSFFAFD#@RDSF!@#')

    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIGKLMNOPQRSTUVWXYZ'))
    if request.GET.get('numbers'):
        characters.extend(list('0123456789'))
    if request.GET.get('special'):
        characters.extend(list('~!@#$%^&*'))

    length = int(request.GET.get('length', 12))
    thepassword = ''
    for x in range(length):
        thepassword += random.choice(characters)
    return render(request, 'generator/password.html', {'password':thepassword})