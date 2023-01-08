from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Card_Main(models.Model):
    user = models.ForeignKey(User, related_name="card_main", on_delete=models.CASCADE)
    # family =  models.ManyToManyField("self",blank=True,null=True)
    # friends =  models.ManyToManyField("self",blank=True,null=True)
    name = models.CharField(max_length=50)
    lname = models.CharField(max_length=60,blank=True,null=True)
    fathername = models.CharField(max_length=60,blank=True,null=True)
    brith_year = models.IntegerField(blank=True, null=True)
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

class Work(models.Model):
    card_work = models.ForeignKey(Card_Main, related_name="work", on_delete=models.CASCADE)
    company_name = models.CharField(max_length=35, blank=True,null=True)   
    position = models.CharField(max_length=60, blank=True,null=True) 
    company_address_city = models.CharField(max_length=55,blank=True,null=True)
    company_address_street = models.CharField(max_length=55,blank=True,null=True)

    
class Color(models.Model):
    colors = models.CharField(max_length=36,blank=True,null=True)  

    def __str__(self) -> str:
        return self.colors  

class Car(models.Model):
    card_cars = models.ForeignKey(Card_Main, related_name="car", on_delete=models.CASCADE)
    car_color = models.ForeignKey(Color, related_name="car",on_delete=models.DO_NOTHING,blank=True,null=True)
    car_name = models.CharField(max_length=35,blank=True,null=True)
    car_number = models.CharField(max_length=9,blank=True,null=True)

    def __str__(self) -> str:
        if self.car_color:
            return str(self.card_cars.name)+' '+self.car_name+' '+' '+str(self.car_color.colors)+ ' ' + self.car_number 
        return str(self.card_cars.name)+' '+self.car_name

class Car_Model(models.Model):
    car = models.OneToOneField(Car, related_name="car_model",on_delete=models.CASCADE, primary_key=True)
    carModels = models.CharField(max_length=35,blank=True,null=True)

    def __str__(self) -> str:
        return self.carModels

class Home(models.Model):
    card_home = models.ForeignKey(Card_Main, related_name="home", on_delete=models.CASCADE)
    home_address_city = models.CharField(max_length=45,blank=True,null=True) 
    home_address_street = models.CharField(max_length=45,blank=True,null=True)   
    home_number = models.CharField(max_length=30,blank=True,null=True)



class Comments(models.Model):
    card_comment = models.OneToOneField(Card_Main, related_name='comments',on_delete=models.CASCADE, primary_key=True)
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
    account = models.CharField(max_length=65,blank=True,null=True)

class Instagram(models.Model):
    card_instagram = models.ForeignKey(Card_Main, related_name="instagram", on_delete=models.CASCADE)
    account  = models.CharField(max_length=65,blank=True,null=True)

class Facebook(models.Model):
    card_facebook = models.ForeignKey(Card_Main, related_name="facebook", on_delete=models.CASCADE)
    account  = models.CharField(max_length=65,blank=True,null=True)



