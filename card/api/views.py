from card.api.serializer import *
from rest_framework.response import Response
from rest_framework.views import APIView
from card.api.permisson import MyPermissons
from rest_framework import status
from card.models import *

class CardApi(APIView):
    # permission_classes = [MyPermissons]

    def get(self, request, format=None):
        all = Card_Main.objects.all()
        all = CardSerializer(all, many=True, context={'request':request})
        return Response(data=all.data)

    def post(self, request, format=None):
        user1=request.user.pk
        data=request.data
        print(data,'+++++++++++++++++++++++++')
        data.update({'user':user1})
        serial = CreateCardSerializer(data=data)
        if serial.is_valid():
            serial.save()
            Response(serial.data, status=status.HTTP_201_CREATED)  
        return Response()   
