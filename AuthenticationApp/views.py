from django.shortcuts import render, redirect
from django.views.generic import View
from .forms import *

# Create your views here.

class Login(View):
  template = 'login.html'
  context = {}
  def get(self, request):
    self.context = {
      "loginForm" : LoginForm()
    }
    return render(request=request, template_name= self.template, context=self.context)