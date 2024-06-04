from django.shortcuts import render,HttpResponse
from .models import News
from .forms import RegistrationForm
# Create your views here.
def NewsP(request):
    obj = News.objects.get(id=1)
    context={
        # "list" : ["python","Django","php","laravel"],
        # "newslist":51
        "data":obj
    }
    return render(request,'news.html',context)

def Home(request):
    return render(request,"home.html")

def Contact(request):
    return render(request,'contact.html')

def NewsDate(request,year):
    article_list = News.objects.filter(pub_date__year = year)

    context = {
        'year':year,
        'article_list':article_list
    }
    return render(request,'newsdate.html',context)
    
def SignUp(request):
    context = {
        "form": RegistrationForm
    }
    return render(request,'registration.html',context)