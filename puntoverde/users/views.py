from http.client import HTTPMessage
from pyexpat.errors import messages
from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm
from django.views.generic.edit import FormView
from django.urls import reverse_lazy,reverse
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import login,logout
from django.http import JsonResponse
from django.contrib import auth
from django import forms
from .forms import InputPassword
from .models import CuentaAdmin




class FormLogin(AuthenticationForm):
    error_messages = {
         'invalid_login':  ("Algunas de tus crendenciales son incorrectos. Porfavor vuelva a ingresarlos")
    }
    def __init__(self, *args, **kwargs):
        super(FormLogin, self).__init__(*args, **kwargs)
    
   

class Login(FormView):
    template_name =  "users/login.html"
    form_class = FormLogin
    success_url = reverse_lazy("market:home")
    
    @method_decorator(csrf_protect)
    @method_decorator(never_cache)
    def dispatch(self,request,*args,**kwars):
        if request.user.is_authenticated:
            return HttpResponseRedirect(self.get_success_url())
        else:

            return super(Login,self).dispatch(request,*args,**kwars)
    
    def form_valid(self,form):
        login(self.request, form.get_user())

        return super(Login,self).form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.method == 'POST':
            context["error_message"] = True  
            return context
        return context


def logoutUser(request):
    if request.user.is_authenticated:
        logout(request)
        return HttpResponseRedirect("../login")
    else:
        return HttpResponseRedirect("../login")


def loginVentaStatus(request):
    error_message = "Has introducio mal el codigo. Vuelva a intentarlo"
    form = InputPassword()
    if request.method == "GET":
        form = InputPassword(request.GET)
        if form.is_valid():
            permiso = CuentaAdmin.objects.get(pk=1)
            password = permiso.password
            if password == form.cleaned_data['password']:
                return HttpResponseRedirect("../admin/")
            else:
                return render(request, 'users/loginStatus.html',context={'error_message': error_message})
    return render(request, 'users/loginStatus.html')




