import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')

import django
django.setup() 

## FAKE POP Scripts
import random

from first_app.models import User
from faker import Faker

fakegen=Faker()



#def add_User():
##    t = Topic.objects.get_or_create(top_name=random.choice(topics))[0]
#    t.save()
#    return t


def populate(N=5):

    for entry in range(N):
     
        # Create fake data for that entry 
        fake_first = fakegen.first_name()
        fake_last = fakegen.last_name()
        fake_email = fakegen.company_email()

        # Create new webpage entry_points

        adduser= User.objects.get_or_create(first_name=fake_first,last_name=fake_last,email=fake_email)[0]

        # Create fake access record for webpage entry_points

        #acc_rec = AccessRecord.objects.get_or_create(name=webpage,date=fake_date)[0]

if __name__ == '__main__':
    print ("populating scripts")
    populate(20)
    print ("populating complete")