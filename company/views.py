from django.shortcuts import render
from rest_framework.generics import RetrieveUpdateAPIView,ListAPIView,CreateAPIView,ListCreateAPIView
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
    
class CompanyDetail(ListAPIView):  
    serializer_class = CompanyListSerializer  
    def get_queryset(self):
        return Company.objects.filter(is_available=True,user_id=self.kwargs.get('user_id'))  
    
class JobAdd(ListCreateAPIView): 
    queryset = JobPost.objects.filter(is_available=True) 
    filter_backends = (SearchFilter,)
    search_fields = ("Job_titile", "job_discription","Experiance","job_type", "requerd_skills")
    serializer_class = JobPostSerializer   
    
class JobListUser(ListAPIView): 
    queryset = JobPost.objects.filter(is_available=True) 
    filter_backends = [SearchFilter]
    search_fields = ['Job_title','salary','Experience','job_type','posted_date','company_id__Location','company_id__company_name']
    serializer_class = JobPostListSerializer       

class JobUpdate(RetrieveUpdateAPIView):
    queryset =JobPost.objects.filter(is_available=True)   
    serializer_class = JobPostSerializer  

class JobList(ListAPIView):    
    # queryset = JobPost.objects.filter(is_available=True ) 
    serializer_class = JobPostListSerializer 
    def get_queryset(self):
        return JobPost.objects.filter(is_available=True,company_id=self.kwargs.get('company_id'))
       