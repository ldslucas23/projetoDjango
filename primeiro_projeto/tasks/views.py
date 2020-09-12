from django.shortcuts import render
from django.http import HttpResponse

#Ao chamar o /helloworld ele vai cair nessa view
def helloWorld(request):
    return HttpResponse('Hello World')
