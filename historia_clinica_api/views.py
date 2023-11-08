from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Historia
from .serializer import HistoriaSerializer
from rest_framework import status

# Create your views here.

class PacientesApiView(APIView):
    def get(self):
        pacientes = Historia.objects.all()
        serializer = HistoriaSerializer(pacientes, many=True)
        return Response({"message": "success", "pacientes": serializer.data}, status=status.HTTP_200_OK) 
    
    
class HistoriasApiView(APIView):
    def get(self, id=0):
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
