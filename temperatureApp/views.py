from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import TemperatureData
from .serializers import TemperatureDataSerializer


# Create your views here.
def index(request):
    return render(request, 'index.html')


class TemperatureDataView(APIView):
    @staticmethod
    def get():
        temperature_data = TemperatureData.objects.all()
        serializer = TemperatureDataSerializer(temperature_data, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @staticmethod
    def post(request):
        serializer = TemperatureDataSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
