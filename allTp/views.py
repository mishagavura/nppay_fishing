from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from django.views.generic import DetailView, UpdateView, DeleteView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.utils import timezone
import datetime
from django.core.mail import send_mail

# Create your views here.



def login_in(request):
	return render(request, 'allTp/home.html')