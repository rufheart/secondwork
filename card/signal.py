from django.apps import AppConfig
from django.db.models.signals import post_save
from card.models import Card_Main, About,Home,Phone,Work,Car,Tiktok,Instagram,Facebook
from django.dispatch import receiver


id=0
ab=0
status = []
@receiver(post_save)
def created_card(sender, instance, created=False, **kwargs):
    global id  
    global status
    if created: 
        lists = ['Card_Main','Phone','Work','Home','Tiktok','Instagram','Facebook','Car']
        if sender.__name__ == 'Card_Main':
            id = instance.id
            About.objects.create(card_about=instance)
            
        for alfa in lists:
            if sender.__name__==alfa and id!=0:
                about=About.objects.get(card_about=id)                
                if alfa=='Phone':
                    about.phone=True
                elif alfa=='Work':
                    about.work=True 
                elif alfa=='Home':
                    about.home=True
                elif alfa=='Tiktok':
                    about.tiktok=True 
                elif alfa=='Instagram':
                    about.instagram=True 
                elif alfa=='Facebook':
                    about.facebook=True
                elif alfa=='Car':
                    about.car=True 
                about.save()                             
        else:
            if id!=0:
                about=About.objects.get(card_about=id)
                if about.phone==None:
                    about.phone=False
                    about.save()
                elif about.work==None:
                    about.work=False
                    about.save()
                elif about.home==None:
                    about.home=False
                    about.save()
                elif about.tiktok==None:
                    about.tiktok=False
                    about.save()
                elif about.instagram==None:
                    about.instagram=False
                    about.save()
                elif about.facebook==None:
                    about.facebook=False
                    about.save()   
                elif about.car==None:
                    about.car=False
                    about.save()   
    # if not created:
    #     print(sender.__name__,'not')

