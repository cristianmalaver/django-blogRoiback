from ast import Import
from datetime import datetime
from time import timezone

from urllib import response
from django.contrib.auth.models import User
from django.test import TestCase
from .models import Profile

# Create your tests here.


'''TEST for create users in the models'''


class Prueba(TestCase):
    def test_create_user_model1(self):
        hola = True
        self.assertIs(hola, True)


def test_create_user_model():
    
    user_insert = User(id='2',password='pbkdf2_sha256$390000$HXW62Ei0xzmtlVlZtVBX7u$GkD8dhWS3GniJVrZd1q1bnt4VkfDSdt5z830DwvOZUk=',
    last_login='1',is_superuser='1',username='cristianmalaver',last_name='malaver',email='cristianmalaver95@gmail.com',is_staff='1',
    is_active='1',date_joined='2022-08-0503:20:11',first_name='cristian')
    
    return User.objects.create(user_insert)

'''TEST for create profile in the models'''
        
class CreateProfileModel(TestCase):

    def test_create_profile(self):

        
        user = test_create_user_model()
        website='www.hiImaTestCase.com'
        phone_number= '56156165515'
        picture='hola/hola.png'
        Profile(user = user, website = website, phone_number= phone_number, picture = picture)

        self.assertEqual(response.status_code, 200)
