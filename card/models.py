from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Card_Main(models.Model):
    user = models.ForeignKey(User,related_name="card_main", on_delete=models.CASCADE)
    family = models.ForeignKey("self")
    friends = models.ForeignKey("self")
    name = models.CharField(max_length=50)
    lname = models.CharField(max_length=60)
    fathername = models.CharField(max_length=60)
    brith_year = models.IntegerField(max_length=20)
    features = models.TextField()

class Photos(models.Model):
    user_image = models.ForeignKey(Card_Main, related_name="card_main", on_delete=models.CASCADE)
    photo = models.ImageField(blank=True)

class Phone(models.Model):
    ph_numbers_card = models.ForeignKey(Card_Main, related_name="card_main", on_delete=models.CASCADE)
    numbers = models.IntegerField(max_length=15,blank=True)

class Work(models.Model):
    card_work = models.ForeignKey(Card_Main, related_name="card_main", on_delete=models.CASCADE)
    company_name = models.CharField(max_length=35, blank=True)   
    position = models.CharField(max_length=60, blank=True) 
    company_address = models.CharField(max_length=35,blank=True)

class Car_Model(models.Model):
    carModels = models.CharField(max_length=35)

class Color(models.Model):
    colors = models.CharField(max_length=36)    

class Car(models.Model):
    card_cars = models.ForeignKey(Card_Main, related_name="card_main", on_delete=models.CASCADE)
    car_model = models.ForeignKey(Car_Model, related_name="car_model", on_delete=models.CASCADE)
    car_color = models.ForeignKey(Color, related_name="color", on_delete=models.CASCADE)
    car_name = models.CharField(max_length=35, blank=True)
    car_number = models.CharField(max_length=7,blank=True)

class Home(models.Model):
    card_home = models.ForeignKey(Card_Main, related_name="card_main", on_delete=models.CASCADE)
    home_address = models.CharField(max_length=45,blank=True,null=True)    



