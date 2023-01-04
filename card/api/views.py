from card.api.serializer import *
from rest_framework.response import Response
from rest_framework.views import APIView
from card.api.permisson import MyPermissons
from card.models import *

class CardApi(APIView):
    permission_classes = [MyPermissons]

    def get(self, request, format=None):
        all = Card_Main.objects.all()
        all = CardSerializer(all, many=True, context={'request':request})
        return Response(data=all.data)
