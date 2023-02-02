from django.apps import AppConfig
from django.db.models.signals import post_save
from card.models import Card_Main, About,Home,Phone,Work,Car,Tiktok,Instagram,Facebook
from django.dispatch import receiver
foreignkeys = []
all = ['Phone','Home','Work','Car','Tiktok','Facebook','Instagram']
lists = ['Phone','Home','Work','Car','Tiktok','Facebook','Instagram']
@receiver(post_save)
def created_card(sender, instance ,created=False, **kwargs):
    if sender.__name__=='Card_Main':
        card = sender.objects.get(id=instance.id)
        about=About.objects.create(card_about=card)
        if card.name != None:
            about.name = True
            about.save()
        elif card.name == None:
            about.name = False  
            about.save()  
        if card.lname == None:
            about.lname =False
            about.save()
        elif card.lname != None:
            about.lname = True  
            about.save()  
        if card.fathername != None:
            about.father_name = True
            about.save() 
        elif card.fathername == None:
            about.father_name = False
            about.save() 
        if card.birth_year != None:
            about.birth_year = True
            about.save() 
        elif card.birth_year == None:
            about.birth_year = False 
            about.save()        
        if card.features != None:
            about.features = True
            about.save() 
        elif card.features == None:
            about.features = False
            about.save() 
    count = 0
    for one in lists:
        if sender.__name__==one:
            # sd = sender.objects.get(id=instance.id)
            print(instance[0])
            if one in all:

                all.remove(one)
    # if sender.__name__== 'Phone':
    #     phone = sender.objects.get(id=instance.id)
    #     about = About.objects.get(card_about=phone.ph_numbers_card)
    #     about.phone = True
    #     about.save()
    #     if 'Phone' in all:
    #         all.remove('Phone')
    # if sender.__name__=='Home':
    #     home = sender.objects.get(id=instance.id)
    #     about = About.objects.get(card_about=home.card_home)
    #     about.home = True
    #     about.save()
    #     if 'Home' in all:
    #         all.remove('Home')
    # if sender.__name__=='Work':
    #     work = sender.objects.get(id=instance.id)
    #     about = About.objects.get(card_about=work.card_work)
    #     about.work = True
    #     about.save()
    #     if 'Work' in all:
    #         all.remove('Work')
    # if sender.__name__=='Car':
    #     car = sender.objects.get(id=instance.id)
    #     about = About.objects.get(card_about=car.card_cars)  
    #     about.car = True
    #     about.save() 
    #     if 'Car' in all: 
    #         all.remove('Car')
    # if sender.__name__=='Tiktok':
    #     tiktok = sender.objects.get(id=instance.id)
    #     about = About.objects.get(card_about=tiktok.card_tiktok)  
    #     about.tiktok = True
    #     about.save() 
    #     if 'Tiktok' in all: 
    #         all.remove('Tiktok')      
    # if sender.__name__=='Facebook':
    #     facebook = sender.objects.get(id=instance.id)
    #     about = About.objects.get(card_about=facebook.card_facebook)  
    #     about.facebook = True
    #     about.save() 
    #     if 'Facebook' in all: 
    #         all.remove('Facebook')  
    # if sender.__name__=='Instagram':
    #     instagram = sender.objects.get(id=instance.id)
    #     about = About.objects.get(card_about=instagram.card_instagram)  
    #     about.instagram = True
    #     about.save() 
    #     if 'Instagram' in all: 
    #         all.remove('Instagram')                          
    if sender.__name__=='Card_Main':
        for one in all:
            if one == 'Phone':
                about = About.objects.get(card_about = instance)   
                about.phone = False 
                about.save()

            if one == 'Work':
                about = About.objects.get(card_about = instance)   
                about.work = False 
                about.save()   

            if one == 'Home':
                about = About.objects.get(card_about = instance)   
                about.home = False 
                about.save()     

            if one == 'Car':
                about = About.objects.get(card_about = instance)   
                about.car = False 
                about.save()

            if one == 'Tiktok':
                about = About.objects.get(card_about = instance)   
                about.tiktok = False 
                about.save()        

            if one == 'Facebook':
                about = About.objects.get(card_about = instance)   
                about.facebook = False 
                about.save()   

            if one == 'Instagram':
                about = About.objects.get(card_about = instance)   
                about.instagram = False 
                about.save()                                                        
    print(all)    