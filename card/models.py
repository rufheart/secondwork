from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Card_Main(models.Model):
    user = models.ForeignKey(User, related_name="card_main", on_delete=models.CASCADE)
    family = models.ForeignKey("self", on_delete=models.CASCADE)
    # friends = models.ForeignKey("self", on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    lname = models.CharField(max_length=60)
    fathername = models.CharField(max_length=60)
    brith_year = models.IntegerField(blank=True, null=True)
    features = models.TextField()

class Photos(models.Model):
    user_image = models.ForeignKey(Card_Main, related_name="images", on_delete=models.CASCADE)
    photo = models.ImageField(blank=True)

class Phone(models.Model):
    ph_numbers_card = models.ForeignKey(Card_Main, related_name="phone", on_delete=models.CASCADE)
    numbers = models.IntegerField(blank=True)

class Work(models.Model):
    card_work = models.ForeignKey(Card_Main, related_name="work", on_delete=models.CASCADE)
    company_name = models.CharField(max_length=35, blank=True)   
    position = models.CharField(max_length=60, blank=True) 
    company_address = models.CharField(max_length=35,blank=True)

class Car_Model(models.Model):
    carModels = models.CharField(max_length=35)
    
class Color(models.Model):
    colors = models.CharField(max_length=36)    

class Car(models.Model):
    card_cars = models.ForeignKey(Card_Main, related_name="car", on_delete=models.CASCADE)
    car_model = models.ForeignKey(Car_Model, related_name="car", on_delete=models.CASCADE)
    car_color = models.ForeignKey(Color, related_name="car", on_delete=models.CASCADE)
    car_name = models.CharField(max_length=35, blank=True)
    car_number = models.CharField(max_length=7,blank=True)

class Home(models.Model):
    card_home = models.ForeignKey(Card_Main, related_name="home", on_delete=models.CASCADE)
    home_address = models.CharField(max_length=45,blank=True,null=True)    

class Comments(models.Model):
    card_comment = models.OneToOneField(Card_Main, on_delete=models.CASCADE, primary_key=True)
    user_comment = models.ForeignKey(User, related_name="comments", on_delete=models.CASCADE)
    comments = models.TextField(blank=True,null=True)

class About(models.Model):
    card_about = models.OneToOneField(Card_Main, related_name="card_main1",on_delete=models.CASCADE)  
    name = models.BooleanField()
    lanme = models.BooleanField()
    father_name = models.BooleanField()
    birth_year = models.BooleanField()
    features = models.BooleanField()
    family = models.BooleanField()
    friends = models.BooleanField()
    facebook = models.BooleanField()
    tiktok = models.BooleanField()
    instagram = models.BooleanField()
    images = models.BooleanField()
    phone = models.BooleanField()
    home = models.BooleanField()
    work = models.BooleanField()
    car = models.BooleanField()

class tiktok(models.Model):
    card_tiktok = models.ForeignKey(Card_Main, related_name="tiktok", on_delete=models.CASCADE)
    account = models.CharField(max_length=35,blank=True)

class instagram(models.Model):
    card_instagram = models.ForeignKey(Card_Main, related_name="instagram", on_delete=models.CASCADE)
    account  = models.CharField(max_length=35, blank=True)

class facebook(models.Model):
    card_facebook = models.ForeignKey(Card_Main, related_name="facebook", on_delete=models.CASCADE)
    account  = models.CharField(max_length=35, blank=True)



