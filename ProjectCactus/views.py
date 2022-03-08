from audioop import reverse
from cmath import log
import imp
import re
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout

def hello(request):
    return render(request,'home.html')

