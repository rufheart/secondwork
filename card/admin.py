from django.contrib import admin
from .models import *

class PhotoAdmin(admin.TabularInline):
    model = Photos
    

@admin.register(Card_Main)
class CardAdmin(admin.ModelAdmin):
    inlines = [PhotoAdmin]
    fields = ('user','name','lname','fathername','birth_year','features','family','friends')


admin.site.register((About,Photos,Phone,Work,Car,Color,ChooseCars,Car_Model,Home,Comments,Tiktok,Instagram,Facebook))
