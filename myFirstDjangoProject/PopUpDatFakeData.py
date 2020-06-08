import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','myFirstDjangoProject.settings')

import django
django.setup()

import random
from myFirstDjangoApp.models import Topic,Page,Access
from faker import Faker

fakeDataGen=Faker()
topics=['Search','Marketing','Learning','News','Games']


def add_topic():
    t=Topic.objects.get_or_create(t_name='News')
    t.save()
    return t
    
def populate(N=8):
    for entry in range(N):
        top=add_topic()
        date=fakeDataGen.date()
        name=fakeDataGen.text()
        webpg=Page.objects.get_or_create(p_topic=top,p_name=name)[0]
        acc=Access.objects.get_or_create(a_name=webpg,a_date=date)[0]
        
if  __name__== '__main__':
    print("!!!!!!! POPULAING FAKE DATA !!!!!!!")
    populate(15)
    print("@@@@@@@ POPULAING COMPLETE @@@@@@@")