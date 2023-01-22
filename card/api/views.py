from card.api.serializer import *
from rest_framework.response import Response
from rest_framework.views import APIView
from card.api.permisson import MyPermissons
from rest_framework.permissions import AllowAny
from rest_framework import status
from django.http import Http404
from card.models import *

class CardApi(APIView):
    permission_classes = [AllowAny]

    def get(self, request, format=None):
        card = Card_Main.objects.all()
        serializer = CardSerializer(card, many=True, context={'request':request})
        return Response(data=serializer.data)

    def post(self, request, format=None):
        print(ChooseCars.objects.all()[0])
        # user1=request.user.pk
        user1 = User.objects.all()[0].id
        data=request.data
        print(user1,'+++++++++++++++++++++++++')
        data.update({'user':user1})
        serializer = CreateCardSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            Response(serializer.data, status=status.HTTP_201_CREATED)  
        else:
            print(serializer.errors)
        return Response()   

class UpdateCard(APIView):
    def get_object(self, pk):
        try:
            return Card_Main.objects.get(pk=pk)
        except Card_Main.DoesNotExist:
            raise Http404

    def get(self, request,pk, **kwargs):
        card = self.get_object(pk)
        serializer = CardSerializer(card, context={'request':request})
        return Response(data=serializer.data)
    
    def put(self, request, pk, format=None):
        card = self.get_object(pk)
        data=request.data
        user = request.user.id
        data.update({"user":user})
        serializer = UpdateCardSerializerPut(card, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
    def patch(self, request, pk, **kwargs):
        card = self.get_object(pk)
        serializer = UpdateCardSerializer(card, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)    
    
    def delete(self, request, pk, **kwargs):
        card = self.get_object(pk)
        card.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)