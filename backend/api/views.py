from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response

class TecnologiasView(APIView):
    def get(self, request):
        tecnologias = [
            {"id": 1, "nombre": "Python", "tipo": "Backend"},
            {"id": 2, "nombre": "React", "tipo": "Frontend"},
        ]
        return Response(tecnologias)
    
    
class ProyectosView(APIView):
    def get(self, request):
        # Código para manejar la solicitud GET
        pass

    def post(self, request):
        # Código para manejar la solicitud POST
        pass   