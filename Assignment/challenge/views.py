import requests
from django.shortcuts import render


def index(request):
    
    url='http://api.worldbank.org/v2/datacatalog?format=json'
    res=requests.get(url.format()).json()
    print(res)
    context={'res':res}

    return render(request,'all/index.html',context)