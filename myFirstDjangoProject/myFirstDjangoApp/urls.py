from django.conf.urls import url
from myFirstDjangoApp import views

urlpatterns = [

    url(r'^$', views.index,name='index'),
    
]
