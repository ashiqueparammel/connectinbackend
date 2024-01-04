from rest_framework.serializers import ModelSerializer
from company.serializers import JobPostListSerializer
from users.serializers import CommonSkillsSerializer, userDataSerializer
from .models import Education, EmployeeProfile, PersonalSkills, ReportJobPost, SavedPost, job_Applications

class EmployeeProfileSerializer(ModelSerializer):
    class Meta:
        model = EmployeeProfile
        fields ='__all__'
class PersonalSkillsListSerializer(ModelSerializer):
    skills = CommonSkillsSerializer()
    class Meta:
        model = PersonalSkills    
        fields = '__all__'         
           
class EmployeeProfileDetail_Serializer(ModelSerializer):
    profile =PersonalSkillsListSerializer(source='personal_skills',many=True)
    user= userDataSerializer()
    class Meta:
        model = EmployeeProfile
        fields ='__all__'

class SavePostSerializer(ModelSerializer):
    class Meta:
        model = SavedPost
        fields ='__all__'
        
class DetailSavePostSerializer(ModelSerializer):
    job_post = JobPostListSerializer()
    class Meta:
        model = SavedPost
        fields ='__all__'        
class EducationSerializer(ModelSerializer):
    class Meta:
        model = Education
        fields ='__all__'        

class PersonalSkillsSerializer(ModelSerializer):
    class Meta:
        model = PersonalSkills
        fields ='__all__'                

class job_ApplicationsSerializer(ModelSerializer):
    class Meta:
        model = job_Applications
        fields ='__all__'                
        
class MyJobsListSerializer(ModelSerializer):
    
    profile = EmployeeProfileDetail_Serializer()
    job_post = JobPostListSerializer()
    class Meta:
        model = job_Applications
        fields ='__all__'    



class ReportJobPostSerializer(ModelSerializer):
    
    class Meta:
        model = ReportJobPost
        fields ='__all__'    

class ReportJobPostListSerializer(ModelSerializer):
    user = userDataSerializer()
    Post = JobPostListSerializer()
    class Meta:
        model = ReportJobPost
        fields ='__all__'        