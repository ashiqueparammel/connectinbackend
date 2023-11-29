from rest_framework.serializers import ModelSerializer
from users.serializers import userDataSerializer
from .models import Education, EmployeeProfile, PersonalSkills, SavedPost, job_Applications

class EmployeeProfileSerializer(ModelSerializer):
    # user_id = userDataSerializer()
    class Meta:
        model = EmployeeProfile
        fields ='__all__'

class SavePostSerializer(ModelSerializer):
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