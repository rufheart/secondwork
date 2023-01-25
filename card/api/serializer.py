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
    print('colors serialize isledi')
    class Meta:
        model = Color
        fields = ['id','colors']

class ChooseCarSerialize(serializers.ModelSerializer):
    class Meta:
        model = ChooseCars
        fields = ['id','name']        

class CarModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car_Model
        fields = ['id','carModels']        

class CarSerializer(serializers.ModelSerializer):
    car_color = ColorSerialize()
    choose_car = ChooseCarSerialize()
    car_model = CarModelSerializer()
    class Meta:
        model = Car
        fields = ['choose_car','car_color','car_model','car_number',]        

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
    id = serializers.IntegerField(required=False)
    class Meta:
        model = Phone
        fields = ['id','numbers']      
         

class WorkSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
    class Meta:
        model = Work
        fields = ['id','company_name','position','company_address']

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
        fields = ['id','user','name','family','lname','fathername','birth_year','features','car','home','comments','phone','work','images','tiktok','instagram','facebook',]


class CreateCardSerializer(serializers.ModelSerializer):
    phone = PhoneSerializer(many=True)
    home = HomeSerializer(many=True)
    work = WorkSerializer(many=True)
    car  = CarSerializer(many=True)
    images = PhotosSerializer(many=True)
    tiktok = TiktokSerializer(many=True)
    instagram = InstagramSerializer(many=True)
    facebook = FacebookSerializer(many=True)
    
    
    def create(self, validated_data):
        phones_data= validated_data.pop("phone")
        works_data = validated_data.pop("work")
        homes_data = validated_data.pop("home")
        cars_data = validated_data.pop("car")
        tiktoks_data = validated_data.pop("tiktok")
        instagrams_data = validated_data.pop("instagram")
        facebooks_data = validated_data.pop("facebook")
        user_images = validated_data.pop("images")
        family = validated_data.pop('family')
        card = Card_Main.objects.create(**validated_data)
        
        for i in family:
            if i != card:
                card.family.add(i)
                card.save()
        
        for phone_data in phones_data:
            Phone.objects.create(ph_numbers_card=card,**phone_data)
        for work_data in works_data:
            Work.objects.create(card_work=card,**work_data) 
        for home_data in homes_data:
            Home.objects.create(card_home=card,**home_data) 
        for tiktok_data in tiktoks_data:
            Tiktok.objects.create(card_tiktok=card,**tiktok_data)
        for instagram_data in instagrams_data:
            Instagram.objects.create(card_instagram=card,**instagram_data)
        for facebook_data in facebooks_data:
            Facebook.objects.create(card_facebook=card,**facebook_data)
        for user_image in user_images:
            Photos.objects.create(user_image=card,**user_image)

        for car_data in cars_data:
            select = ChooseCars.objects.get(id=car_data['choose_car']['name'])
            if car_data['car_model']['carModels']:
                data_car = Car_Model.objects.get(id=car_data['car_model']['carModels'])
                if select.id==data_car.car_model.id:
                    car_model = Car_Model.objects.get(id=car_data['car_model']['carModels'])
                else:
                    car_model=None
            else:
                car_model=None
            if car_data['car_color']['colors']:
                car_color = Color.objects.get(id=car_data['car_color']['colors']) 
            else:
                car_color = None
            car_data.update({"choose_car":select,"car_color":car_color,"car_model":car_model})
            Car.objects.create(card_cars=card,**car_data)
        return card

    class Meta:
        model = Card_Main
        fields = ['user','name','family', 'lname','fathername','birth_year','features','phone','work','car','home','tiktok','instagram','facebook','images']   


class UpdateCardSerializerPut(serializers.ModelSerializer):
    phone = PhoneSerializer(many=True)
    home = HomeSerializer(many=True)
    work = WorkSerializer(many=True)
    car  = CarSerializer(many=True)
    images = PhotosSerializer(many=True)
    tiktok = TiktokSerializer(many=True)
    instagram = InstagramSerializer(many=True)
    facebook = FacebookSerializer(many=True)
  

    def update(self, instance, validated_data):   
        card = Card_Main.objects.get(id=instance.id) 
        print(card)
        phones_data= validated_data.pop("phone")
        print(phones_data,'++++++++++++++')
        phones = (instance.phone).all()
        print(phones,'phonesssssssssssuudp')
        phones = list(phones)
        works_data = validated_data.pop("work")
        works = (instance.work).all()
        works = list(works)
        homes_data = validated_data.pop("home")
        homes = (instance.home).all()
        homes = list(homes)
        cars_data = validated_data.pop("car")
        cars = (instance.car).all()
        cars = list(cars)
        tiktoks_data = validated_data.pop("tiktok")
        tiktoks = (instance.tiktok).all()
        tiktoks = list(tiktoks)
        instagrams_data = validated_data.pop("instagram")
        instagrams = (instance.instagram).all()
        instagrams = list(instagrams)
        facebooks_data = validated_data.pop("facebook")
        facebooks = (instance.facebook).all()
        facebooks = list(facebooks)
        user_images = validated_data.pop("images")
        users = (instance.images).all()
        users = list(users)
        # family = validated_data.pop('family')
        instance.name = validated_data.get("name", instance.name)   
        instance.lname = validated_data.get("lname", instance.lname)  
        instance.fathername = validated_data.get("fathername", instance.fathername)
        instance.birth_year = validated_data.get("birth_year", instance.birth_year)
        instance.features = validated_data.get("features", instance.features)
        fmly = validated_data.get("family", instance.family)
        families = (instance.family).all()
        families = list(families)
        for i in fmly:
            instance.family.add(i)
        instance.save()
        keep_phones_id = []
        keep_works_id = []
        keep_homes_id = []
        keep_tiktoks_id = []
        keep_fbs_id = []
        keep_instgrms_id = []
        ids = [c.id for c in phones]
        print(ids,'idssssss')
        for phone_data in phones_data:
            if "id" in phone_data.keys():
                if Phone.objects.filter(id=phone_data["id"],ph_numbers_card=card).exists():
                    c = Phone.objects.get(id=phone_data["id"])
                    print(c,'ccccc')
                    c.numbers = phone_data.get('numbers', c.numbers)
                    c.save()
                    keep_phones_id.append(c.id)
                else:
                    continue
            else:
                c=Phone.objects.create(ph_numbers_card=card,**phone_data)
                keep_phones_id.append(c.id)
        for ph in phones:
            print(phones,1)
            if ph.id not in keep_phones_id:
                ph.delete()
            print(phones,2)    
        for work_data in works_data:
            if  "id" in work_data.keys():   
                if  Work.objects.filter(id=work_data["id"],card_work=card).exists():
                    c=Work.objects.get(id=work_data["id"])
                    c.company_name = work_data.get('company_name', c.company_name)
                    c.position = work_data.get('position', c.position)
                    c.company_address = work_data.get('company_address', c.company_address)
                    c.save()
                    keep_works_id.append(c.id)
                else:
                    continue
            else:
                c=Work.objects.create(card_work=card, **work_data)
                keep_works_id.append(c.id)          
        for wk in works:
            if wk.id not in keep_works_id:
                wk.delete()         
        for home_data in homes_data:
            if "id" in home_data.keys():
                if Home.objects.filter(id=home_data["id"],card_home=card):
                    c=Home.objects.get(id=home_data["id"])
                    c.home_address = homes.get("home_address", c.home_address)
                    c.save()
                    keep_homes_id.append(c.id)
                else:
                    continue
            else:
                c=Home.objects.create(card_home=card, **home_data)
                keep_homes_id(c.id)
        for hm in homes:
            if hm.id not in keep_homes_id:
                hm.delete()
        for tiktok_data in tiktoks_data:
            if "id" in tiktok_data.keys():
                if Tiktok.objects.filter(id=tiktok_data["id"], card_tiktok=card):
                    c = Tiktok.objects.get(id=tiktok_data["id"])
                    c.account = tiktok_data.get("account", c.account)
                    c.save()
                    keep_tiktoks_id.append(c.id)
                else:
                    continue
            else:
                c = Tiktok.objects.create(card_tiktok=card, **tiktok_data)
                keep_tiktoks_id.append(c.id)    
        for tk in tiktoks:
            if tk.id not in keep_tiktoks_id:
                tk.delete()

        for facebook_data in facebooks_data:
            if "id" not in facebook_data.keys():
                if Facebook.objects.filter(id=facebook_data["id"], card_facebook=card):
                    c = Facebook.objects.get(id=facebook_data["id"])
                    c.account = facebook_data.get("account", c.account)
                    c.save()
                    keep_fbs_id.append(c.id)
                else:
                    continue
            else:
                c = Facebook.objects.create(card_facebook=card, **facebook_data)
                keep_fbs_id.append(c.id)
        for fb in facebooks:
            if fb.id not in keep_fbs_id:
                fb.delete()                
        for instagram_data in instagrams_data:
            if "id" in instagram_data.keys():
                if Instagram.objects.filter(id=instagram_data["id"], card_instagram=card):
                    c = Instagram.objects.get(id=instagram_data["id"])
                    c.account = instagram_data.get("account", c.account)
                    c.save()
                    keep_instgrms_id.append(c.id)
                else:
                    continue
            else:
                c=Instagram.objects.create(card_instagram=card)
                keep_instgrms_id.append(c.id)
        for inst in instagrams:
            if inst.id not in keep_instgrms_id:
                inst.delete()                
        for car_data in cars_data:
            if "id" in car_data.keys():
                if Car.objects.filter(id=car_data["id"],card_cars=card):
                    c=Car.objects.get(id=car_data["id"])
                    c.car_color=car_data.get("car_color", c.car_color)
                    c.choose_car=car_data.get("choose_car", c.choose_car)
                    c.car_model = car_data.get("car_model", c.car_model)
                    c.car_number = car_data
            # car = cars.pop(0)
            # color= car_data.get("car_color")
            # car.car_color = Color.objects.get(id=color['colors'])
            # choose= car_data.get("choose_car")
            # ch = ChooseCars.objects.get(id=choose['name'])
            # car.choose_car = ChooseCars(id=choose['name']) 
            # model = car_data.get("car_model")
            # md = Car_Model.objects.get(id=model['carModels'])
            # if ch.id == md.car_model.id:
            #     car.car_model = Car_Model.objects.get(id=model['carModels'])
            # else: 
            #     car.car_model = None   
            # car.car_number = car_data.get("car_number")
            # car.save()                   
        for user_image in user_images:
            img = user_images.pop(0)
            img.photo = user_image.get("photo")
            img.save()           
        return instance
        
    

    class Meta:
        model =Card_Main
        fields = ['user','name','family', 'lname','fathername','birth_year','features','phone','work','car','home','tiktok','instagram','facebook','images']   
        read_only_fields = ['user']

class UpdateCardSerializer(serializers.ModelSerializer):
    phone = PhoneSerializer(many=True)
    home = HomeSerializer(many=True)
    work = WorkSerializer(many=True)
    car  = CarSerializer(many=True)
    images = PhotosSerializer(many=True)
    tiktok = TiktokSerializer(many=True)
    instagram = InstagramSerializer(many=True)
    facebook = FacebookSerializer(many=True)
    
    

    def update(self, instance, validated_data):
        tenda_data = validated_data.copy()
        if validated_data.get("phone"):
            print('if islediii')
            phones_data= validated_data.pop("phone")
            phones = (instance.phone).all()
            phones = list(phones)
            print(phones, 'phonesssssssssssssss')
        if validated_data.get("work"):    
            works_data = validated_data.pop("work")
            works = (instance.work).all()
            works = list(works)
        if validated_data.get("home"):
            homes_data = validated_data.pop("home")
            homes = (instance.home).all()
            homes = list(homes)    
        if validated_data.get("car"):
            cars_data = validated_data.pop("car")
            cars = (instance.car).all()
            cars = list(cars)    
        if validated_data.get("tiktok"):
            tiktoks_data = validated_data.pop("tiktok")
            tiktoks = (instance.tiktok).all()
            tiktoks = list(tiktoks)
        if validated_data.get("instagram"):
            instagrams_data = validated_data.pop("instagram")
            instagrams = (instance.instagram).all()
            instagrams = list(instagrams)
        if validated_data.get("facebook"):
            facebooks_data = validated_data.pop("facebook")
            facebooks = (instance.facebook).all()
            facebooks = list(facebooks) 
        if validated_data.get("images"):
            user_images = validated_data.pop("images")
            users = (instance.images).all()
            users = list(users)   
        if validated_data.get("family"):
            family = validated_data.pop('family')
            families = (instance.family).all()
            families = list(families)         
        instance.name = validated_data.get("name", instance.name)   
        instance.lname = validated_data.get("lname", instance.lname)  
        instance.fathername = validated_data.get("fathername", instance.fathername)
        instance.birth_year = validated_data.get("birth_year", instance.birth_year)
        instance.features = validated_data.get("features", instance.features)
        instance.save()

        if tenda_data.get("phone"):
            print('if ilsedi2')
            for phone_data in phones_data: 
                pho = phones.pop(0)
                pho.numbers = phone_data.get("numbers")
                pho.save()
        if tenda_data.get("work"):
            for work_data in works_data:    
                wor = works.pop(0)
                wor.company_name = work_data.get("company_name")   
                wor.position = work_data.get("position")
                wor.company_address = work_data.get("company_address")   
                wor.save()   
        if tenda_data.get("home"):
            for home_data in homes_data:
                hom = homes.pop(0)
                hom.home_address = home_data.get("home_address")
                hom.save()
        if tenda_data.get("tiktok"):
            for tiktok_data in tiktoks_data:
                tik = tiktoks.pop(0)
                tik.account = tiktok_data.get("account")
                tik.save() 
        if tenda_data.get("instagram"):
            for instagram_data in instagrams_data:
                ins = instagrams.pop(0)
                ins.account = instagram_data.get("account")
                ins.save()    
        if tenda_data.get("facebook"):
            for facebook_data in facebooks_data:
                fac = facebooks.pop(0)
                fac.account = facebook_data.get("account")
                fac.save()
        if tenda_data.get("car"):
            for car_data in cars_data:
                car = cars.pop(0)
                color= car_data.get("car_color")
                car.car_color = Color.objects.get(id=color['colors'])
                choose= car_data.get("choose_car")
                ch = ChooseCars.objects.get(id=choose['name'])
                car.choose_car = ChooseCars.objects.get(id=choose['name']) 
                model = car_data.get("car_model")
                md = Car_Model.objects.get(id=model['carModels'])
                print(ch,md.car_model)
                if ch.id == md.car_model.id:
                    car.car_model = Car_Model.objects.get(id=model['carModels'])
                else: 
                    car.car_model = None    
                car.car_number = car_data.get("car_number")
                car.save()                            
        return instance
    



    class Meta:
        model =Card_Main
        fields = ['user','name','family', 'lname','fathername','birth_year','features','phone','work','car','home','tiktok','instagram','facebook','images']   
        read_only_fields = ['user']
      
      
