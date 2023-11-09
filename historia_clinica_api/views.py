from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Historia
from .serializer import HistoriaSerializer
from rest_framework import status
import requests
import json

# Create your views here.

class HistoriasApiView(APIView):
    def get(self, request, id=0):
        if id>0:
            try:
                historia=Historia.objects.get(id=id)
                serializer=HistoriaSerializer(historia)
                data={
                    "message":"Historia encontrado",
                    "historia":serializer.data
                }
                return Response(data, status=status.HTTP_200_OK)
            except Historia.DoesNotExist:
                return Response({"message":"Historia no encontrada"}, status=status.HTTP_404_NOT_FOUND)
        else:
            historia = Historia.objects.all()
            serializer = HistoriaSerializer(historia, many=True)
            return Response({"message" :"succes","historia": serializer.data}, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = HistoriaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Historia creada correctamente"   }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, id):
        historia = Historia.objects.get(id=id)
        serializer = HistoriaSerializer(historia, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "historia actualizada correctamente"   }, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, id):
        historia = Historia.objects.get(id=id)
        historia.delete()
        return Response({"message": "Historia eliminada correctamente"   }, status=status.HTTP_200_OK)

#consumir api para obtener los usuarios    
class PacientesApiView(APIView):
    def get(self, request):
        url = 'https://rickandmortyapi.com/api/character/'
        response = requests.get(url)
        data = response.json()        
        return Response(data)
