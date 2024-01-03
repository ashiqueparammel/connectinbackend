from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateAPIView,ListAPIView,RetrieveUpdateDestroyAPIView, DestroyAPIView,RetrieveAPIView
from .models import Education, EmployeeProfile, PersonalSkills, SavedPost, job_Applications
from .serializers import DetailSavePostSerializer, EducationSerializer, EmployeeProfileDetail_Serializer, EmployeeProfileSerializer, MyJobsListSerializer, PersonalSkillsListSerializer, PersonalSkillsSerializer, SavePostSerializer, job_ApplicationsSerializer
# from rest_framework.filters import SearchFilter


class EmployeeProfileAdd(ListCreateAPIView):
    queryset = EmployeeProfile.objects.all()
    serializer_class = EmployeeProfileSerializer

class EmployeeProfileDetail(ListAPIView):  
    serializer_class = EmployeeProfileDetail_Serializer  
    def get_queryset(self):
        # print(self.kwargs.get('user_id'),'check my user id')
        return EmployeeProfile.objects.filter(user=self.kwargs.get('user'))      
    
class EmployeeProfileUpdate(RetrieveUpdateAPIView):
    
    queryset = EmployeeProfile.objects.all() 
    serializer_class = EmployeeProfileSerializer   

class SavePostAdd(ListCreateAPIView):
    queryset = SavedPost.objects.filter(is_available=True)
    serializer_class = SavePostSerializer
    
class UserSavePostDetail(ListAPIView):
    serializer_class = DetailSavePostSerializer    
    def get_queryset(self):
        return SavedPost.objects.filter(is_available=True,user=self.kwargs.get('user'))      
    
class SavePostUpdate(RetrieveUpdateDestroyAPIView):
    queryset = SavedPost.objects.filter(is_available=True)
    serializer_class = SavePostSerializer

class EducationAdd(ListCreateAPIView):
    queryset = Education.objects.filter(is_available=True)
    serializer_class = EducationSerializer

class ListPersonalEducation(ListAPIView):
    serializer_class = EducationSerializer
    def get_queryset(self):
        return Education.objects.filter(profile=self.kwargs.get('profile'))   
    
class EducationUpdate(RetrieveUpdateDestroyAPIView):
    queryset = Education.objects.filter(is_available=True)
    serializer_class = EducationSerializer
         
class PersonalSkillsAdd(ListCreateAPIView):
    queryset = PersonalSkills.objects.all()
    serializer_class = PersonalSkillsSerializer
    
class PersonalSkillsUpdate(RetrieveUpdateAPIView):
    queryset = PersonalSkills.objects.all()
    serializer_class = PersonalSkillsSerializer
    
class ListPersonalSkills(ListAPIView):
    serializer_class = PersonalSkillsListSerializer
    def get_queryset(self):
        return PersonalSkills.objects.filter(profile=self.kwargs.get('profile'))   
    
class RemovePersonalSkills(DestroyAPIView):
    queryset = PersonalSkills.objects.all()
    serializer_class =  PersonalSkillsSerializer

class job_ApplicationsAdd(ListCreateAPIView):
    queryset = job_Applications.objects.all()
    serializer_class = job_ApplicationsSerializer
    
class job_ApplicationsUpdate(RetrieveUpdateAPIView):
    queryset = job_Applications.objects.all()
    serializer_class = job_ApplicationsSerializer  
      
class job_ApplicationsListPersonal(ListAPIView):
    serializer_class = job_ApplicationsSerializer   
    def get_queryset(self):
        return job_Applications.objects.filter(profile=self.kwargs.get('profile'))
    
class MyApplicationList(ListAPIView):
    serializer_class = MyJobsListSerializer   
    def get_queryset(self):
        return job_Applications.objects.filter(job_post=self.kwargs.get('job_post'))    

class MySingleJobsList(RetrieveAPIView):
    queryset = job_Applications.objects.all()   
    serializer_class = MyJobsListSerializer 

class MySingleJobsListRead(ListAPIView):
    serializer_class = MyJobsListSerializer   
    def get_queryset(self):
        return job_Applications.objects.filter(Read=True, job_post=self.kwargs.get('job_post'))

class MySingleJobsListUnRead(ListAPIView):
    serializer_class = MyJobsListSerializer   
    def get_queryset(self):
        return job_Applications.objects.filter(Read=False,job_post=self.kwargs.get('job_post'))
    
class MyJobsList(ListAPIView):
    serializer_class = MyJobsListSerializer   
    def get_queryset(self):
        return job_Applications.objects.filter(profile=self.kwargs.get('profile'))      