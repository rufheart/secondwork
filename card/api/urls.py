from card.api.views import *
from django.urls import path

urlpatterns = [
    path('card/', CardApi.as_view(),name='card_api'),
     path('card/<int:pk>/', UpdateCard.as_view(),name='card_api'),
     path('car/',CarApi.as_view(), name='car_api'),
     path('car/<pk>/',CarApiPK.as_view(),name='car_pk'),
     path('model/<pk>/', Model_CarPK.as_view(), name = 'model'),
     path('colors/',ColorApi.as_view(), name='colors_api')
]