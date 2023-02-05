from django.apps import AppConfig
from django.db.models.signals import post_save
from card.models import Card_Main, About,Home,Phone,Work,Car,Tiktok,Instagram,Facebook
from django.dispatch import receiver

id=0
@receiver(post_save)
def created_card(sender, instance ,created=False, **kwargs):
    if created:
        lists = ['Phone','Work','Home','Tiktok','Instagram','Facebook','Car']
        global id        
        if sender.__name__ == 'Card_Main':
            About.objects.create(card_about=instance)
            id = instance.id
        for alfa in lists:
            if sender.__name__==alfa:
                if alfa=='Phone' and id!=0:
                    about=About.objects.get(card_about=id)
                    about.phone=True
                    about.save() 
                if alfa=='Work' and id!=0:
                    about=About.objects.get(card_about=id)
                    about.work=True
                    about.save() 
                if alfa=='Home' and id!=0:
                    about=About.objects.get(card_about=id)
                    about.home=True
                    about.save()
                if alfa=='Tiktok' and id!=0:
                    about=About.objects.get(card_about=id)
                    about.tiktok=True
                    about.save() 
                if alfa=='Instagram' and id!=0:
                    about=About.objects.get(card_about=id)
                    about.instagram=True
                    about.save() 
                if alfa=='Facebook' and id!=0:
                    about=About.objects.get(card_about=id)
                    about.facebook=True
                    about.save()
                if alfa=='Car' and id!=0:
                    about=About.objects.get(card_about=id)
                    about.car=True
                    about.save()                          
        else:
            if id!=0:
                about=About.objects.get(card_about=id)
                if about.phone==None:
                    about.phone=False
                    about.save()
                if about.work==None:
                    about.work=False
                    about.save()
                if about.home==None:
                    about.home=False
                    about.save()
                if about.tiktok==None:
                    about.tiktok=False
                    about.save()
                if about.instagram==None:
                    about.instagram=False
                    about.save()
                if about.facebook==None:
                    about.facebook=False
                    about.save()   
                if about.car==None:
                    about.car=False
                    about.save()                                                                                                                       
                                                                                                                     







