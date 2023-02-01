from django.apps import AppConfig
from django.db.models.signals import post_save
from card.models import Card_Main, About,Home,Phone,Work,Car,Tiktok,Instagram,Facebook
from django.dispatch import receiver

# @receiver(post_save, sender=Card_Main)
@receiver(post_save)
def created_card(sender, instance ,created=False, **kwargs):
    if sender.__name__=='Card_Main':
        card = sender.objects.get(id=instance.id)
        about=About.objects.create(card_about=card)
        print(sender)
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

    if sender.__name__== 'Phone':
        phone = sender.objects.get(id=instance.id)
        about = About.objects.get(card_about=phone.ph_numbers_card)
        about.phone = True
        about.save()