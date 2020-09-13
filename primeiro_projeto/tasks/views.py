from django.shortcuts import render
from django.http import HttpResponse

#Ao chamar o /helloworld ele vai cair nessa view
def helloWorld(request):
    return HttpResponse('Hello World')

def taskList(request):
    return render(request, 'tasks/list.html')

#Nessa view ele recebe o name como parâmetro
def yourName(request, name):
    return render(request, 'tasks/yourname.html', {'name' : name})