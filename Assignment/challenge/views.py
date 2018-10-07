import requests
from django.shortcuts import render


def index(request):
    
    url='http://api.worldbank.org/v2/datacatalog?format=json'
    res=requests.get(url)
    data=res.json()
    print(data)
    test = "Working"
    dat_des={
        'name':data['metatype']['name'],
        

    }
    context={'dat_des':dat_des}

    return render(request,'all/index.html',context)


        