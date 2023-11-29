from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateAPIView
from .models import Education, EmployeeProfile, PersonalSkills, SavedPost, job_Applications
from .serializers import EducationSerializer, EmployeeProfileSerializer, PersonalSkillsSerializer, SavePostSerializer, job_ApplicationsSerializer
# from rest_framework.filters import SearchFilter


class EmployeeProfileAdd(ListCreateAPIView):
    queryset = EmployeeProfile.objects.all()
    serializer_class = EmployeeProfileSerializer
    
class EmployeeProfileUpdate(RetrieveUpdateAPIView):
    queryset = EmployeeProfile.objects.all() 
    serializer_class = EmployeeProfileSerializer   

class SavePostAdd(ListCreateAPIView):
    queryset = SavedPost.objects.filter(is_available=True)
    serializer_class = SavePostSerializer
    
class SavePostUpdate(RetrieveUpdateAPIView):
    queryset = SavedPost.objects.filter(is_available=True)
    serializer_class = SavePostSerializer

class EducationAdd(ListCreateAPIView):
    queryset = Education.objects.filter(is_available=True)
    serializer_class = EducationSerializer
    
class EducationUpdate(RetrieveUpdateAPIView):
    queryset = Education.objects.filter(is_available=True)
    serializer_class = EducationSerializer
         
class PersonalSkillsAdd(ListCreateAPIView):
    queryset = PersonalSkills.objects.filter(is_available=True)
    serializer_class = PersonalSkillsSerializer
    
class PersonalSkillsUpdate(RetrieveUpdateAPIView):
    queryset = PersonalSkills.objects.filter(is_available=True)
    serializer_class = PersonalSkillsSerializer

class job_ApplicationsAdd(ListCreateAPIView):
    queryset = job_Applications.objects.all()
    serializer_class = job_ApplicationsSerializer
    
class job_ApplicationsUpdate(RetrieveUpdateAPIView):
    queryset = job_Applications.objects.all()
    serializer_class = job_ApplicationsSerializer    