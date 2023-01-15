from card.models import *
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from django.contrib.auth import get_user_model

User = get_user_model()



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id","username","image"]

class ColorSerialize(serializers.ModelSerializer):
    class Meta:
        model = Color
        fields = ['colors']

# class CarModelSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Car_Model
#         fields = ['carModels']        

class CarSerializer(serializers.ModelSerializer):
    car_color = ColorSerialize()
    # car_model = CarModelSerializer()
    class Meta:
        model = Car
        fields = ['car_name','car_color','car_number',]        

class HomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Home
        fields = ['home_address']   

class CommentSerializer(serializers.ModelSerializer):
    user_comment = UserSerializer()
    class Meta:
        model = Comments
        fields = ['user_comment','comments']

class PhoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Phone
        fields = ['numbers']      
         

class WorkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Work
        fields = ['company_name','position','company_address']

class PhotosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photos
        fields = ['photo']

class FacebookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Facebook
        fields = ['account']        

class InstagramSerializer(serializers.ModelSerializer):
    class Meta:
        model = Instagram
        fields = ['account']     

class TiktokSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tiktok
        fields = ['account']                   

class CardSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    car = CarSerializer(many=True)
    home = HomeSerializer(many =True)
    comments = CommentSerializer()
    phone = PhoneSerializer(many =True)
    work = WorkSerializer(many = True)
    images = PhotosSerializer(many = True)
    tiktok = TiktokSerializer(many = True)
    instagram = InstagramSerializer(many = True)
    facebook = FacebookSerializer(many = True)
    class Meta:
        model=Card_Main
        fields = ['id','user','name','lname','fathername','brith_year','features','car','home','comments','phone','work','images','tiktok','instagram','facebook']

# class CreateCarSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Car
#         fields = ['card_cars','car_name','car_number']


class CreateCardSerializer(serializers.ModelSerializer):
    phone = PhoneSerializer(many=True)
    home = HomeSerializer(many=True)
    work = WorkSerializer(many=True)
    car  = CarSerializer(many=True)
    # images = PhotosSerializer()
    tiktok = TiktokSerializer(many=True)
    instagram = InstagramSerializer(many=True)
    facebook = FacebookSerializer(many=True)



    
    def create(self, validated_data):
        print("create function")
        phones_data= validated_data.pop("phone")
        works_data = validated_data.pop("work")
        homes_data = validated_data.pop("home")
        cars_data = validated_data.pop("car")
        tiktoks_data = validated_data.pop("tiktok")
        instagrams_data = validated_data.pop("instagram")
        facebooks_data = validated_data.pop("facebook")
        print(phones_data,works_data,homes_data)
        card = Card_Main.objects.create(**validated_data)
        for phone_data in phones_data:
            Phone.objects.create(ph_numbers_card=card,numbers=phone_data['numbers'])
        for work_data in works_data:
            Work.objects.create(card_work=card,company_name=work_data['company_name'],position=work_data['position'],company_address=work_data['company_address'])
        for home_data in homes_data:
            Home.objects.create(card_home=card,home_address=home_data['home_address']) 
        for car_data in cars_data:
            Car.objects.create(card_cars=card,car_name=car_data['car_name'],car_number=car_data['car_number'])     
        for tiktok_data in tiktoks_data:
            Tiktok.objects.create(card_tiktok=card,account=tiktok_data['account'])
        for instagram_data in instagrams_data:
            Instagram.objects.create(card_instagram=card,account=tiktok_data['account'])
        for facebook_data in facebooks_data:
            Facebook.objects.create(card_facebook=card,account=tiktok_data['account'])


        return card

    class Meta:
        model = Card_Main
        fields = ['user','name','lname','fathername','brith_year','features','phone','work','car','home','tiktok','instagram','facebook']   


