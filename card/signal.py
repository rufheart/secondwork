from django.apps import AppConfig
from django.db.models.signals import post_save,pre_save
from card.models import Card_Main, About,Home,Phone,Work,Car,Tiktok,Instagram,Facebook
from django.dispatch import receiver


id=0
ab=0
status = []
@receiver(post_save)
def created_card(sender, instance, created=False, **kwargs):
    if sender.__name__ == 'Card_Main':
        pass
    global id  
    # print(ab)
    if created: 
        # print(sender.__name__,'created')
        # print(sender.__name__,'created')
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
    if not created:
        global status
        print(status)
    
        if sender.__name__=='Card_Main':
            id = instance.id
            status=[]
        about=About.objects.get(card_about=id)
        if Phone.objects.filter(card_phones=id).first()==None and 'Phone' not in status:
   
            status.append('Phone')
            about.phone=False
            about.save()
        if Work.objects.filter(card_works=id).first()==None and 'Work' not in status:
   
            status.append('Work')
            about.work=False
            about.save()
        if Home.objects.filter(card_homes=id).first()==None and 'Home' not in status:
   
            status.append('Home')
            about.home=False
            about.save()   
        if Tiktok.objects.filter(card_tiktoks=id).first()==None and 'Tiktok' not in status:
 
            status.append('Tiktok')
            about.tiktok=False
            about.save()         
        if Instagram.objects.filter(card_instagrams=id).first()==None and 'Instagram' not in status:
         
            status.append('Instagram')
            about.instagram=False
            about.save()  
        if Facebook.objects.filter(card_facebooks=id).first()==None and 'Facebook' not in status:
      
            status.append('Facebook')
            about.facebook=False
            about.save()                                              
                                               



