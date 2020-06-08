from django.http import HttpResponse
from django.shortcuts import render
from myFirstDjangoApp.models import Topic,Page,Access

# Create your views here.
def index(request):
    WebPageList=Access.objects.order_by('a_date')
    WebPagesDict={"WebPageList":WebPageList}
    return render(request,"myFirstDjangoApp/employee.html",context=WebPagesDict)
     