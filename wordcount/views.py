from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
#    return HttpResponse('hello')
    return render(request, 'home.html',{'hithere':'This is me'})

def count(request):
    fulltext = request.GET['fulltext']
    wordlist = fulltext.split()

    worddictionary = {}
    for word in wordlist:
        worddictionary[word] = worddictionary.get(word, 0)+1
    sortedwords = sorted(worddictionary.items(), key = lambda elm:elm[1], reverse = True)
    return render(request, 'count.html',{'fulltext': fulltext,'count':len(wordlist), 'sortedwords': sortedwords})

def about(request):
    return render(request, 'about.html')
