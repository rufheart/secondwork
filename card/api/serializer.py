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
    id = serializers.IntegerField(required=False)
    class Meta:
        model = Color
        fields = ['id','colors']

class ChooseCarSerialize(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
    class Meta:
        model = ChooseCars
        fields = ['id','name']        

class CarModelSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
    class Meta:
        model = Car_Model
        fields = ['id','carModels']        

class CarSerializer(serializers.ModelSerializer):
    car_color = ColorSerialize(required=False)
    choose_car = ChooseCarSerialize()
    car_model = CarModelSerializer(required=False)
    id = serializers.IntegerField(required=False)
    class Meta:
        model = Car
        fields = ['id', 'choose_car','car_color','car_model','car_number',]        

class HomeSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
    class Meta:
        model = Home
        fields = ['id', 'home_address']   

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
    id = serializers.IntegerField(required=False)
    class Meta:
        model = Photos
        fields = ['id', 'photo']

class FacebookSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
    class Meta:
        model = Facebook
        fields = ['id', 'account']        

class InstagramSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
    class Meta:
        model = Instagram
        fields = ['id', 'account']     

class TiktokSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
    class Meta:
        model = Tiktok
        fields = ['id', 'account']                   

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
        phones_data= validated_data.pop("phone")
        phones = (instance.phone).all()
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
        fmly = validated_data.get("family", instance.family)  #Bu hissesin put-a bax
        families = (instance.family).all()
        families = list(families)
        if validated_data.get("family"): 
            print('family isledi')   
            for i in fmly:
                instance.family.add(i)  
        else:
            for i in families:
                instance.family.remove(i) 
        instance.save()
        keep_phones_id = []
        keep_works_id = []
        keep_homes_id = []
        keep_tiktoks_id = []
        keep_fbs_id = []
        keep_instgrms_id = []
        keep_cars_id = []
        keep_images_id = []
        ids = [c.id for c in phones]
        for phone_data in phones_data:
            if "id" in phone_data.keys():
                if Phone.objects.filter(id=phone_data["id"],ph_numbers_card=card).exists():
                    c = Phone.objects.get(id=phone_data["id"])
                    print(type(phone_data))
                    c.numbers = phone_data.get('numbers', c.numbers)
                    c.save()
                    keep_phones_id.append(c.id)
                else:
                    continue
            else:
                c=Phone.objects.create(ph_numbers_card=card,**phone_data)        #Bu daxil edilen datanin idsi olmasa yeni data yaradir
                keep_phones_id.append(c.id)
        for ph in phones:
            if ph.id not in keep_phones_id:     #Eger evvleceden olan deyerin ve ya deyerlerin id-si burda olazsa hemin deyeri yaxud deyerleri silir
                ph.delete()    
        for work_data in works_data:
            print('work isledi')
            if  "id" in work_data.keys():   
                if  Work.objects.filter(id=work_data["id"],card_work=card).exists():
                    c=Work.objects.get(id=work_data["id"])
                    if work_data.get('company_name') != "":
                        c.company_name = work_data.get('company_name', c.company_name)
                    elif work_data.get('company_name') == "":
                        c.company_name = None    
                    if work_data.get('position') != "":
                        c.position = work_data.get('position', c.position)
                    if work_data.get('company_address') == "":
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
                    c.home_address = home_data.get("home_address", c.home_address)
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
                c=Instagram.objects.create(card_instagram=card, **instagram_data)
                keep_instgrms_id.append(c.id)
        for inst in instagrams:
            if inst.id not in keep_instgrms_id:
                inst.delete()    

        for facebook_data in facebooks_data:
            if "id" in facebook_data.keys():
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
        for car_data in cars_data:
            if "id" in car_data.keys():
                if Car.objects.filter(id=car_data["id"],card_cars=card):
                    c=Car.objects.get(id=car_data["id"])
                    if car_data['car_color'] !={}:
                        car_color = Color.objects.get(id=car_data['car_color']['colors'])
                        c.car_color=car_color
                    elif car_data['car_color'] =={}:
                        c.car_color = None
                    car_choose = ChooseCars.objects.get(id=car_data['choose_car']['name'])
                    c.choose_car=car_choose
                    if car_data['car_model'] !={}:
                        mod = Car_Model.objects.get(id=car_data['car_model']['carModels'])                  
                        if car_choose.id == mod.car_model.id:
                            c.car_model = mod
                        else:
                            c.car_model=None    
                    elif car_data['car_model'] == {}:
                        c.car_model = None
                    if car_data.get("car_number") !="":     
                        c.car_number = car_data.get("car_number", c.car_number)
                    elif car_data.get("car_number") =="":
                        c.car_number = None
                    c.save()
                    keep_cars_id.append(c.id)
                else:
                    continue
            else:
                c=Car.objects.create(card_cars=card, **car_data)
                keep_cars_id.append(c.id)
        for cr in cars:
            print('car -----')
            if cr.id not in keep_cars_id:
                cr.delete()                                 
        for user_image in user_images:
            if "id" in user_image.keys():
                if Photos.objects.filter(id=user_image["id"], user_image=card):
                    c=Photos.objects.get(id=user_image["id"])
                    c.save()
                    keep_images_id.append(c.id)
                else:
                    continue
            else:
                c=Photos.objects.create(user_image=card, **user_image)
                keep_images_id.append(c.id)     
        for user_im in users:
            if user_im.id not in keep_images_id:
                user_im.delete()        
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
        print(tenda_data)
        card = Card_Main.objects.get(id=instance.id) 
        if validated_data.get("phone"):
            phones_data= validated_data.pop("phone")
        phones = (instance.phone).all()
        phones = list(phones)
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
        instance.name = validated_data.get("name", instance.name)   
        instance.lname = validated_data.get("lname", instance.lname)  
        instance.fathername = validated_data.get("fathername", instance.fathername)
        instance.birth_year = validated_data.get("birth_year", instance.birth_year)
        instance.features = validated_data.get("features", instance.features)
        if validated_data.get("family"):
            fmly = validated_data.pop("family", instance.family)
        families = (instance.family).all()
        families = list(families)
        if tenda_data.get("family"): 
            print('family isledi')   
            for i in fmly:
                instance.family.add(i)  
        else:
            for i in families:
                instance.family.remove(i)             
        instance.save()
        keep_phones_id = []
        keep_works_id = []
        keep_homes_id = []
        keep_tiktoks_id = []
        keep_fbs_id = []
        keep_instgrms_id = []
        keep_cars_id = []
        keep_images_id = []
        ids = [c.id for c in phones]
        if tenda_data.get("phone"):
            for phone_data in phones_data:
                if "id" in phone_data.keys():
                    if Phone.objects.filter(id=phone_data["id"],ph_numbers_card=card).exists():
                        c = Phone.objects.get(id=phone_data["id"])
                        c.numbers = phone_data.get('numbers', c.numbers)
                        c.save()
                        keep_phones_id.append(c.id)
                    else:
                        continue
                else:
                    c=Phone.objects.create(ph_numbers_card=card,**phone_data)
                    keep_phones_id.append(c.id)
        elif tenda_data.get("phone") == []:
            phone = Phone.objects.filter(ph_numbers_card=card)
            phone.delete()
        else:
            for ph in range(len(phones)):
                phs = phones.pop(0)
                phs.save()
        for ph in phones:
            if ph.id not in keep_phones_id:
                ph.delete()    
        if tenda_data.get("work"):         
            for work_data in works_data:
                if  "id" in work_data.keys():   
                    if  Work.objects.filter(id=work_data["id"],card_work=card).exists():
                        c=Work.objects.get(id=work_data["id"])
                        if work_data.get('company_name') !="":
                            c.company_name = work_data.get('company_name', c.company_name)
                        elif work_data.get('company_name')=="":
                            c.company_name = None    
                        if work_data.get('position') !="":
                            c.position = work_data.get('position', c.position)
                        elif work_data.get('position') =="":
                            c.position = None    
                        if work_data.get('company_address')!="":
                            c.company_address = work_data.get('company_address', c.company_address)
                        elif work_data.get('company_address') == "":
                            c.company_address = None
                        c.save()
                        keep_works_id.append(c.id)
                    else:
                        continue
                else:
                    c=Work.objects.create(card_work=card, **work_data)
                    keep_works_id.append(c.id)   
        elif tenda_data.get("work") == []:
            work = Work.objects.filter(card_work=card)
            work.delete()
        else:
            for wk in range(len(works)):
                wks = works.pop(0)
                wks.save()                       
        for wk in works:
            if wk.id not in keep_works_id:
                wk.delete()   
        if tenda_data.get("home"):                      
            for home_data in homes_data:
                if "id" in home_data.keys():
                    if Home.objects.filter(id=home_data["id"],card_home=card):
                        c=Home.objects.get(id=home_data["id"])
                        c.home_address = home_data.get("home_address", c.home_address)
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
        if tenda_data.get("tiktok"):                           
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
        elif tenda_data.get("tiktok") == []:
            tiktok = Tiktok.objects.filter(card_tiktok=card)
            tiktok.delete()
        else:
            for t in range(len(tiktoks)):
                tki = tiktoks.pop(0)
                tki.save()
                             
        for tk in tiktoks:
            if tk.id not in keep_tiktoks_id:
                tk.delete()

        if tenda_data.get("instagram"):
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
                    c=Instagram.objects.create(card_instagram=card, **instagram_data)
                    keep_instgrms_id.append(c.id)
        elif tenda_data.get("instagram")==[]:
            instag = Instagram.objects.filter(card_instagram=card)
            instag.delete()
        else:
            for ins in range(len(instagrams)):
                inss =  instagrams.pop(0)
                inss.save()           
        for inst in instagrams:
            if inst.id not in keep_instgrms_id:
                inst.delete() 

        if tenda_data.get("facebook"):
            for facebook_data in facebooks_data:
                if "id" in facebook_data.keys():
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
        elif tenda_data.get("facebook")==[]:
            face = Facebook.objects.filter(card_facebook=card)
            face.delete()
        else:
            for fb in range(len(facebooks)):
                fbs = facebooks.pop(0)
                fbs.save()            
        for fb in facebooks:
            if fb.id not in keep_fbs_id:
                fb.delete()  

        if tenda_data.get("car"): 
            print('car')             
            for car_data in cars_data:
                print(car_data)
                if "id" in car_data.keys():
                    if Car.objects.filter(id=car_data["id"],card_cars=card):
                        c=Car.objects.get(id=car_data["id"])
                        if car_data['car_color'] != {}:
                            if car_data['car_color']['colors'] != "----":
                                car_color = Color.objects.get(id=car_data['car_color']['colors'])
                                c.car_color=car_color
                        elif car_data['car_color'] == {}:  
                            c.car_color = None     
                        # elif car_data['car_color']['colors'] == "----":   
                        #     c.car_color = None   
                        car_choose = ChooseCars.objects.get(id=car_data['choose_car']['name'])
                        c.choose_car=car_choose
                        if car_data['car_model'] !={}:
                            if car_data['car_model']["carModels"] != "----":
                                mod = Car_Model.objects.get(id=car_data['car_model']['carModels'])                  
                                if car_choose.id == mod.car_model.id:
                                    c.car_model = mod
                                else:
                                    c.car_model=None   
                            elif car_data["car_model"]["carModels"] == "----":
                                c.car_model = None 
                        elif car_data['car_model'] =={}:
                            c.car_model=None
                        if car_data.get("car_number") !="":     
                            c.car_number = car_data.get("car_number", c.car_number)
                        elif car_data.get("car_number") =="":
                            c.car_number = None
                        c.save()
                        keep_cars_id.append(c.id)
                    else:
                        continue
                else:
                    c=Car.objects.create(card_cars=card, **car_data)
                    keep_cars_id.append(c.id)
        elif tenda_data.get("car") == []:
            car=Car.objects.filter(card_cars=card)
            car.delete()
        else:
            for cr in range(len(cars)):
                crs = cars.pop(0)
                crs.save()
        for cr in cars:
            if cr.id not in keep_cars_id:
                cr.delete()
        if tenda_data.get("images"):                                 
            for user_image in user_images:
                if "id" in user_image.keys():
                    if Photos.objects.filter(id=user_image["id"], user_image=card):
                        c=Photos.objects.get(id=user_image["id"])
                        c.save()
                        keep_images_id.append(c.id)
                    else:
                        continue
                else:
                    c=Photos.objects.create(user_image=card, **user_image)
                    keep_images_id.append(c.id)   
        elif tenda_data.get("images"):
            images = Photos.objects.filter(user_image=card)
            images.delete()             
        for user_im in users:
            if user_im.id not in keep_images_id:
                user_im.delete()        
        return instance    


    class Meta:
        model =Card_Main
        fields = ['user','name','family', 'lname','fathername','birth_year','features','phone','work','car','home','tiktok','instagram','facebook','images']   
        read_only_fields = ['user']
      
      
