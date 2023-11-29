from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateAPIView
from .serializers import CompanySerializer, JobPostSerializer
from .models import Company, JobPost
from rest_framework.filters import SearchFilter


class CompanyAdd(ListCreateAPIView):
    queryset = Company.objects.filter(is_available=True) 
    serializer_class = CompanySerializer
    
class CompanyUpdate(RetrieveUpdateAPIView):
    queryset = Company.objects.filter(is_available=True) 
    serializer_class = CompanySerializer   
    
class JobAdd(ListCreateAPIView):
    queryset = JobPost.objects.filter(is_available=True) 
    filter_backends = (SearchFilter,)
    search_fields = ("__all__")
    serializer_class = JobPostSerializer   

class JobUpdate(RetrieveUpdateAPIView):
    queryset =JobPost.objects.filter(is_available=True)   
    serializer_class = JobPostSerializer  
    