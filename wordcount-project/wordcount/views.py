from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render
import operator
def registration(request):
    return HttpResponse('give details')

def home(request):
    return render(request, 'design.html',{'data1':'Type the person name'})

def patients(request):
    return HttpResponse('patients')

def data(request):
    return HttpResponse('data')

def count(request):
	data2 = request.GET['patient']
	wordlist = data2.split()
	values = {}
	for word in wordlist:
		if word in values:
			values[word]+=1
		else:
			values[word]=1
	sorty = sorted(values.items(),key=operator.itemgetter(1),reverse=True)
	return render(request, 'count.html',{'fulltext':data2,'count':len(wordlist),'worddictionary':sorty})

def about(request):
	return render(request, 'about.html')

def mypy(request):
	return HttpResponseRedirect("http://rohithalla.pythonanywhere.com/")