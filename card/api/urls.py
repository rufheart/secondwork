from card.api.views import *
from django.urls import path

urlpatterns = [
    path('card/', CardApi.as_view(),name='cardapi'),
     path('card/<int:pk>/', UpdateCard.as_view(),name='cardapi')
]