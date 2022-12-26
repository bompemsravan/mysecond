from django.shortcuts import render

from django.http import HttpResponse


def sravan(request):
    return HttpResponse('<b>sravan is silent guy</b>')

def maheshbabu(request):
    return HttpResponse('<h2><bold><marquee><i>maheshbabu is called as superstar</marquee></i></h2></bold>')
