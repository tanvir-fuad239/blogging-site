from django.shortcuts import render,HttpResponseRedirect
from django.urls import reverse
from django.http import HttpResponse

def home(request):

    return HttpResponseRedirect(reverse('App_Blog:blog_list'))