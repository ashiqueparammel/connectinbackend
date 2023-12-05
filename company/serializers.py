from rest_framework.serializers import ModelSerializer
from users.serializers import userDataSerializer
from .models import Company, JobPost

class CompanySerializer(ModelSerializer):
    class Meta:
        model = Company
        fields ='__all__'
        
        
class CompanyListSerializer(ModelSerializer):
    user_id = userDataSerializer()
    class Meta:
        model = Company
        fields ='__all__'
        

class JobPostSerializer(ModelSerializer):
    class Meta:
        model = JobPost
        fields = '__all__'

class JobPostListSerializer(ModelSerializer):
    company_id = CompanySerializer()
    class Meta:
        model = JobPost
        fields = '__all__'        