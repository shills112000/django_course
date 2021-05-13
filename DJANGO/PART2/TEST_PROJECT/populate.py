import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'TEST_PROJECT.settings')

import django
django.setup() 

## FAKE POP Scripts
import random

from first_app.models import AccessRecord,Topic,Webpage
from faker import Faker

fakegen=Faker()

topics = ['Search','Social','Marketplace','News','Games']

def add_topic():
    t = Topic.objects.get_or_create(top_name=random.choice(topics))[0]
    t.save()
    return t


def populate(N=5):

    for entry in range(N):
     
        # get topic for entry
        top = add_topic()

        # Create fake data for that entry 
        fake_url = fakegen.url()
        fake_date = fakegen.date()
        fake_name = fakegen.company()

        # Create new webpage entry_points

        webpage= Webpage.objects.get_or_create(topic=top,url=fake_url,name=fake_name)[0]

        # Create fake access record for webpage entry_points

        acc_rec = AccessRecord.objects.get_or_create(name=webpage,date=fake_date)[0]

if __name__ == '__main__':
    print ("populating scripts")
    populate(20)
    print ("populating complete")


