from http.client import HTTPResponse
from django.shortcuts import render, redirect, HttpResponseRedirect
from .models import PersonVote
from django.views.generic import View, DetailView
from django.http import HttpResponse
from django.http import JsonResponse
from .forms import VoteForm, EncuestaForm


class homePage(View):
    template_name = "market/votacion.html"

    def post(self, request, *args, **kwargs):
        form = VoteForm()
        if request.method == "POST":
            form = VoteForm(request.POST)
            if form.is_valid():
                vote = PersonVote()
                vote.vote = form.cleaned_data['vote']
                vote.save()
        return HttpResponseRedirect("encuesta/")

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return(render(request,self.template_name))
        else:
            return redirect("login")




class encuestaPage(View):
    template_name = "market/encuesta.html"


    def post(self, request, *args, **kwargs):
        form = EncuestaForm()
        if request.method == "POST":
            form = EncuestaForm(request.POST)
            if form.is_valid():
                lastet_vote = PersonVote.objects.latest('id')
                lastet_vote.number = form.cleaned_data['number']
                lastet_vote.save()
        return HttpResponseRedirect("../")

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return(render(request,self.template_name))
        else:
            return redirect("login")

class admin(View):
    template_name = "market/admin.html"


    def get(self, request, *args, **kwargs):
        total_votos= PersonVote.objects.all().count()
        happy_votes = PersonVote.objects.filter(vote='happy').count()
        neutral_votes = PersonVote.objects.filter(vote='neutral').count()
        sad_votes = PersonVote.objects.filter(vote='sad').count()
        if total_votos == 0:
            total_votos = 1
        if request.user.is_authenticated:
            context ={
                "count_happy": happy_votes,
                "count_happy_porcentaje": str(round((happy_votes*100)/total_votos,1)) + "%",
                "count_neutral": neutral_votes,
                "count_neutral_porcentaje": str(round((neutral_votes*100)/total_votos,1)) + "%",
                "count_sad": sad_votes,
                "count_sad_porcentaje": str(round((sad_votes*100)/total_votos,1)) + "%",
                "phone_numbers": PersonVote.objects.exclude(number='')
            }
            
            return render(request,self.template_name,context)
        else:
            return redirect("login")

def page_error_404(request,exception):
    return render(request, '404.html')



   
    
    

    

    

