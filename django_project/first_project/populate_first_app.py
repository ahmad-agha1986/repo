import os 
os.environ.setdefault('DJANGO_SETTINGS_MODULE','first_project.settings')

import django

django.setup()

import random

from first_app.models import AccessRecord, Webpage,Topic, Userr
from faker import Faker

fakegen=Faker()
topics=['Search','Social','Marketplace','News','Games']

def add_topic():
	t = Topic.objects.get_or_create(top_name= random.choice(topics))[0]
	t.save()
	return t


def populate(N):

	for entry in range(N):
		top = add_topic()
		fake_url=fakegen.url()
		fake_date=fakegen.date()
		fake_name=fakegen.company()
		fake_first_name=fakegen.first_name()
		fake_last_name= fakegen.last_name()
		fake_email= fakegen.email()

		Webpg = Webpage.objects.get_or_create(topic = top , url= fake_url, webpageName=fake_name)[0]
		acc_rec = AccessRecord.objects.get_or_create(name=Webpg,date=fake_date)[0]
		user = User.objects.get_or_create(First_Name =fake_first_name ,Last_Name= fake_last_name, Email_Address=fake_email)[0]



if __name__ == '__main__':
	print('populating_Script!')
	populate(20)
	print('populating complete!')
