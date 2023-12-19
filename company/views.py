from django.shortcuts import render
from rest_framework.generics import RetrieveUpdateAPIView,ListAPIView,CreateAPIView,ListCreateAPIView
from .serializers import CompanyListSerializer, CompanySerializer, JobPostListSerializer, JobPostSerializer
from .models import Company, JobPost
from rest_framework.filters import SearchFilter,OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend


class CompanyAdd(CreateAPIView):
    queryset = Company.objects.all() 
    serializer_class = CompanySerializer
    
class CompanyListAdd(ListAPIView):
    queryset = Company.objects.filter(is_available=True) 
    serializer_class = CompanyListSerializer    
    
class CompanyUpdate(RetrieveUpdateAPIView):
    queryset = Company.objects.filter(is_available=True) 
    serializer_class = CompanySerializer   
    
class CompanyDetail(ListAPIView):  
    serializer_class = CompanyListSerializer  
    def get_queryset(self):
        # print(self.kwargs.get('user_id'),'check my user id')
        return Company.objects.filter(is_available=True,user_id=self.kwargs.get('user'))  
    
class JobAdd(ListCreateAPIView): 
    queryset = JobPost.objects.filter(is_available=True) 
    filter_backends = (SearchFilter,)
    search_fields = ("Job_titile", "job_discription","Experiance","job_type", "requerd_skills")
    serializer_class = JobPostSerializer   
    
class JobListUser(ListAPIView): 
    queryset = JobPost.objects.filter(is_available=True) 
    filter_backends = [DjangoFilterBackend,SearchFilter,OrderingFilter]
    filterset_fields =[ 'job_type','Experience']
    search_fields = ['Job_title','salary','company_id__Location','company_id__company_name']
    ordering_fields =['posted_date']
    serializer_class = JobPostListSerializer       
    
class JobUserView(RetrieveUpdateAPIView):
    queryset =JobPost.objects.filter(is_available=True)   
    serializer_class = JobPostListSerializer        

class JobUpdate(RetrieveUpdateAPIView):
    queryset =JobPost.objects.filter(is_available=True)   
    serializer_class = JobPostSerializer  

class JobList(ListAPIView):    
    # queryset = JobPost.objects.filter(is_available=True ) 
    serializer_class = JobPostListSerializer 
    def get_queryset(self):
        return JobPost.objects.filter(is_available=True,company=self.kwargs.get('company'))
       