from django.shortcuts import render

from django.http import HttpResponse

def sravani(request):
    return HttpResponse('<b>my name is sravani</b>')

def friends(request):
    return HttpResponse('<i><b><marquee>manju,hari,pavan,sravani,chitti</i></b></marquee>')
