from django.shortcuts import render
from rest_framework.generics import RetrieveUpdateAPIView,ListAPIView,CreateAPIView
from .serializers import CompanyListSerializer, CompanySerializer, JobPostListSerializer, JobPostSerializer
from .models import Company, JobPost
from rest_framework.filters import SearchFilter


class CompanyAdd(CreateAPIView):
    queryset = Company.objects.filter(is_available=True) 
    serializer_class = CompanySerializer
    
class CompanyListAdd(CreateAPIView):
    queryset = Company.objects.filter(is_available=True) 
    serializer_class = CompanyListSerializer    
    
class CompanyUpdate(RetrieveUpdateAPIView):
    queryset = Company.objects.filter(is_available=True) 
    serializer_class = CompanySerializer   
    
class JobAdd(CreateAPIView):
    queryset = JobPost.objects.filter(is_available=True) 
    serializer_class = JobPostSerializer   

class JobUpdate(RetrieveUpdateAPIView):
    queryset =JobPost.objects.filter(is_available=True)   
    serializer_class = JobPostSerializer  

class JobList(ListAPIView) :
    queryset = JobPost.objects.filter(is_available=True) 
    filter_backends = (SearchFilter,)
    search_fields = ("__all__")
    serializer_class = JobPostListSerializer   
       