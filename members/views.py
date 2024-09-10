from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Member


def home_page(request):
    template = loader.get_template("home_page.html")
    return HttpResponse(template.render())


def members(request):
    mymembers = Member.objects.all().values()
    template = loader.get_template("all_members.html")
    context = {"mymembers": mymembers, "owner": "michal"}
    return HttpResponse(template.render(context, request))


def details(request, id):
    mymember = Member.objects.get(id=id)
    template = loader.get_template("details.html")
    context = {
        "mymember": mymember,
    }
    return HttpResponse(template.render(context, request))


def trainer(request):
    template = loader.get_template("trainer.html")
    return HttpResponse(template.render())


def courts(request):
    template = loader.get_template("courts.html")
    return HttpResponse(template.render())
