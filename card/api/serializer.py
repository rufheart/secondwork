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

class CarModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car_Model
        fields = ['carModels']        

class CarSerializer(serializers.ModelSerializer):
    car_color = ColorSerialize()
    car_model = CarModelSerializer()
    class Meta:
        model = Car
        fields = ['id','card_cars','car_name','car_model','car_color',  'car_number',]        

class HomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Home
        fields = ['home_address_city','home_address_street','home_number']   

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
        fields = ['company_name','position','company_address_city','company_address_street']

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
        

class CreateCardSerializer(serializers.ModelSerializer):
    phone = PhoneSerializer()
    # comments = CommentSerializer()
    class Meta:
        model = Card_Main
        fields = ['user','name','lname','fathername','brith_year','features','phone']

    def create(self,request):
        print(request['user'],'request')
        # print(request['phone'],'phone')
        # data = Phone.objects.create(ph_numbers_card_id=33,numbers=request['phone']['numbers'])
        data = Comments.objects.create(card_comment_id=33,user_comment=request['user'],comments=request['comments'][''])

        return request


