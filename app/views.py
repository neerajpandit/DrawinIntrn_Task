from django.shortcuts import render
from rest_framework.response import Response
from .serializers import UserSerializer
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from .models import User


from rest_framework.authentication import  BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
  
class UserView(APIView):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self,request, pk=None, format=None):
        if request.method == 'GET':
            id=pk
            if id is not None:
                stu=User.objects.get(id=id)
                serializer=UserSerializer(stu)
                return Response(serializer.data)
            stu=User.objects.all()
            serializer=UserSerializer(stu,many=True)
        return Response(serializer.data)



    def post(self,request, pk=None):  
     if request.method =='POST':
         serializer=UserSerializer(data=request.data)
         if serializer.is_valid():
             serializer.save()
             return Response({'msg':'User Success'})
         return Response({'msg':'Email already uses'})
     


