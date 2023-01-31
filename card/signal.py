from django.apps import AppConfig
from django.db.models.signals import post_save
from card.models import Card_Main
from django.dispatch import receiver

@receiver(post_save, sender=Card_Main)
def created_card(sender, instance ,created, **kwargs):
    if created:
        print(sender.work,instance)

# post_save.connect(created_card, sender = Card_Main)    