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

class CarCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ['card_cars','car_name','car_number']


class CreateCardSerializer(serializers.ModelSerializer):
    phone = PhoneSerializer(required=False)
    home = HomeSerializer(required=False)
    work = WorkSerializer(required=False)
    # car  = CarCreateSerializer()
    # images = PhotosSerializer()
    tiktok = TiktokSerializer(required=False)
    instagram = InstagramSerializer(required=False)
    facebook = FacebookSerializer(required=False)

    class Meta:
        model = Card_Main
        fields = ['user','name','lname','fathername','brith_year','features','phone','home','work','tiktok','instagram','facebook']
        extra_kwargs = {"instagram": {"required": False, "allow_null": True}}

    
    def create(self,request):
        print('create isledi')
        print(request,'requestsssssssssssssssssssssss')
        # user = User.objects.get(id=request.user.id)
        data1 = Card_Main.objects.create(user = request['user'],name=request['name'])
        id=data1.id
        color = Color.objects.get(id=1)
        Phone.objects.create(ph_numbers_card_id=id,numbers=request['phone']['numbers'])
        Work.objects.create(card_work_id=id,company_name=request['work']['company_name'])
        Home.objects.create(card_home_id=id ,home_address_city=request['home']['home_address_city'])
        # Car.objects.create(card_cars_id=id,car_name=request['car']['car_name'],car_number=request['car']['car_number'])
        # Photos.objects.create(user_image_id=id,photo=request['photo'])
        Tiktok.objects.create(card_tiktok_id=id,account=request['tiktok']['account'])
        Instagram.objects.create(card_instagram_id=id,account=request['instagram']['account'])
        Facebook.objects.create(card_facebook_id=id,account=request['facebook']['account'])

        # print(data,'dattttttttttttttttttttttttttttttttttaaaaaaaaaaaaaaaaaa*********')
        return request


