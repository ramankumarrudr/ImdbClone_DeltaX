import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','imdb_clone.settings')

import django
django.setup()

# FAKE pOP

import random
from app.models import AccessRecord,webPage,Topic
from faker import Faker

fakegen = Faker()
topics = ['Search','SOCIAL','Marketplace']

def add_topics():
    t = Topic.objects.get_or_create(top_name=random.choice(topics))[0]
    t.save()
    return t

def populate(N):
    for entry in range (N):
        top = add_topics()
        fake_url = fakegen.url()
        fake_date = fakegen.date()
        fake_name = fakegen.company()
        # create new web page entry
        webpg = webPage.objects.get_or_create(topic=top,url=fake_url,name=fake_name)[0]
        
        acc_rec = AccessRecord.objects.get_or_create(name=webpg,date = fake_date)

if __name__ == '__main__':
    print("populating script")
    populate(20)
    print("completed")