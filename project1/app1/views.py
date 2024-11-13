from django.shortcuts import render,get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from.serializers import StudentSerializer
from.models import Student

# Create your views here.
class Student_API(APIView):
    def get(self,request,pk=None):
        if pk==None:
            obj=Student.objects.all()
            serializer=StudentSerializer(obj,many=True)
            return Response(data=serializer.data)
        objs=get_object_or_404(Student, id=pk)
        serializer=StudentSerializer(objs)
        return Response(data=serializer.data)
    
    def post(self, request):
        serializer=StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        return Response(data={"msg":"Data is Invalid"})
    
    def put(self, request,pk):
        obj=Student.objects.get(id=pk)
        serializer=StudentSerializer(obj,data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        return Response(data={"msg":"Data is Invalid"})
    
    def delete(self,request,pk):
        obj=get_object_or_404(Student,id=pk)
        obj.delete()
        return Response(data={"msg":"Data Deleted"})