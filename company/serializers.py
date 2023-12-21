from rest_framework.serializers import ModelSerializer
from users.serializers import CommonSkillsSerializer, userDataSerializer
from .models import Company, JobPost, Required_Skills

class CompanySerializer(ModelSerializer):
    class Meta:
        model = Company
        fields ='__all__'
        
        
class CompanyListSerializer(ModelSerializer):
    user = userDataSerializer()
    class Meta:
        model = Company
        fields ='__all__'
        

class JobPostSerializer(ModelSerializer):
    class Meta:
        model = JobPost
        fields = '__all__'
class JobRequired_SkillsSerializer(ModelSerializer):
    class Meta:
        model = Required_Skills    
        fields = '__all__'         
        
class Required_SkillsSerializer(ModelSerializer):
    skills = CommonSkillsSerializer()
    class Meta:
        model = Required_Skills    
        fields = '__all__'       
                      
class JobPostListSerializer(ModelSerializer):
    Required_Skill = Required_SkillsSerializer(source='required_skills',many=True)
    company = CompanyListSerializer()
    class Meta:
        model = JobPost
        fields = '__all__'        

