from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Card_Main(models.Model):
    user = models.ForeignKey(User, related_name="card_main", on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    lname = models.CharField(max_length=60,blank=True,null=True)
    fathername = models.CharField(max_length=60,blank=True,null=True)
    birth_year = models.IntegerField(blank=True, null=True)
    family =  models.ManyToManyField("self", blank=True, null = True, symmetrical=False, related_name='myfamily')
    friends =  models.ManyToManyField("self", blank=True, symmetrical=False, related_name='myfriend')
    features = models.TextField(blank=True, null=True)

    def __str__(self) -> str:
        if self.lname:
            return self.name+' '+self.lname
        return self.name    
        

class Photos(models.Model):
    user_image = models.ForeignKey(Card_Main, related_name="images", on_delete=models.CASCADE)
    photo = models.ImageField(blank=True,null=True)

    def __str__(self) -> str:
        return self.user_image.name

class Phone(models.Model):
    ph_numbers_card = models.ForeignKey(Card_Main, related_name="phone", on_delete=models.CASCADE)
    numbers = models.CharField(max_length=15, blank=True,null=True)

    def __str__(self) -> str:
        return self.numbers

class Work(models.Model):
    card_work = models.ForeignKey(Card_Main, related_name="work", on_delete=models.CASCADE)
    company_name = models.CharField(max_length=35, blank=True,null=True)   
    position = models.CharField(max_length=60, blank=True,null=True) 
    company_address = models.CharField(max_length=55,blank=True,null=True)

    def __str__(self) -> str:
        return self.company_name
    

class Color(models.Model):
    colors = models.CharField(max_length=36,blank=True,null=True)  

    def __str__(self) -> str:
        return self.colors  

class ChooseCars(models.Model):
    name = models.CharField(max_length=40,blank=True,null=True)

    def __str__(self) -> str:
        return self.name 

class Car_Model(models.Model):
    car_model = models.ForeignKey(ChooseCars, related_name="car_model",on_delete=models.CASCADE)
    carModels = models.CharField(max_length=35,blank=True,null=True)



class Car(models.Model):
    card_cars = models.ForeignKey(Card_Main, related_name="car", on_delete=models.CASCADE)
    car_color = models.ForeignKey(Color, related_name="car",on_delete=models.DO_NOTHING, blank=True,null=True)
    choose_car = models.ForeignKey(ChooseCars, related_name="car",on_delete=models.CASCADE)
    car_model = models.ForeignKey(Car_Model, related_name='car',on_delete=models.DO_NOTHING, blank=True,null=True)
    car_number = models.CharField(max_length=9,blank=True,null=True)

    # def __str__(self) -> str:
    #     return self.card_cars 


class Home(models.Model):
    card_home = models.ForeignKey(Card_Main, related_name="home", on_delete=models.CASCADE)
    home_address = models.CharField(max_length=45,blank=True,null=True) 

    def __str__(self) -> str:
        return self.home_address


class Comments(models.Model):
    card_comment = models.OneToOneField(Card_Main, related_name='comments',on_delete=models.CASCADE)
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

class Tiktok(models.Model):
    card_tiktok = models.ForeignKey(Card_Main, related_name="tiktok", on_delete=models.CASCADE)
    account = models.CharField(max_length=65)

    def __str__(self) -> str:
        return self.account

class Instagram(models.Model):
    card_instagram = models.ForeignKey(Card_Main, related_name="instagram", on_delete=models.CASCADE)
    account  = models.CharField(max_length=65)

    def __str__(self) -> str:
        return self.account

class Facebook(models.Model):
    card_facebook = models.ForeignKey(Card_Main, related_name="facebook", on_delete=models.CASCADE)
    account  = models.CharField(max_length=65)

    def __str__(self) -> str:
        return self.account



