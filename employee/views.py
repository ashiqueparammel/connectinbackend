from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateAPIView,
    ListAPIView,
    RetrieveUpdateDestroyAPIView,
    DestroyAPIView,
    RetrieveAPIView,
)
from employee.tasks import test_func
from .models import (
    Education,
    EmployeeProfile,
    PersonalSkills,
    ReportJobPost,
    SavedPost,
    job_Applications,
)
from .serializers import (
    DetailSavePostSerializer,
    EducationSerializer,
    EmployeeProfileDetail_Serializer,
    EmployeeProfileSerializer,
    MyJobsListSerializer,
    PersonalSkillsListSerializer,
    PersonalSkillsSerializer,
    ReportJobPostListSerializer,
    ReportJobPostSerializer,
    SavePostSerializer,
    job_ApplicationsSerializer,
)
from rest_framework.filters import SearchFilter,OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend

class EmployeeProfileAdd(ListCreateAPIView):
    queryset = EmployeeProfile.objects.all()
    serializer_class = EmployeeProfileSerializer


class EmployeeProfileDetail(ListAPIView):
    serializer_class = EmployeeProfileDetail_Serializer

    def get_queryset(self):
        return EmployeeProfile.objects.filter(user=self.kwargs.get("user"))
    
    
class EmployeeListing(ListAPIView):
    queryset = EmployeeProfile.objects.filter(user__is_company=False,user__is_active=True)
    filter_backends = [DjangoFilterBackend,SearchFilter,OrderingFilter]
    filterset_fields =['Location']
    search_fields = ['description','header','Location','user__email','user__username']
    serializer_class = EmployeeProfileDetail_Serializer


class EmployeeProfileUpdate(RetrieveUpdateAPIView):
    queryset = EmployeeProfile.objects.all()
    serializer_class = EmployeeProfileSerializer


class SavePostAdd(ListCreateAPIView):
    queryset = SavedPost.objects.filter(is_available=True)
    serializer_class = SavePostSerializer


class UserSavePostDetail(ListAPIView):
    serializer_class = DetailSavePostSerializer

    def get_queryset(self):
        return SavedPost.objects.filter(is_available=True, user=self.kwargs.get("user"))


class SavePostUpdate(RetrieveUpdateDestroyAPIView):
    queryset = SavedPost.objects.filter(is_available=True)
    serializer_class = SavePostSerializer


class EducationAdd(ListCreateAPIView):
    queryset = Education.objects.filter(is_available=True)
    serializer_class = EducationSerializer


class ListPersonalEducation(ListAPIView):
    serializer_class = EducationSerializer

    def get_queryset(self):
        return Education.objects.filter(profile=self.kwargs.get("profile"))


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
        return PersonalSkills.objects.filter(profile=self.kwargs.get("profile"))


class RemovePersonalSkills(DestroyAPIView):
    queryset = PersonalSkills.objects.all()
    serializer_class = PersonalSkillsSerializer


class job_ApplicationsAdd(ListCreateAPIView):
    queryset = job_Applications.objects.all()
    serializer_class = job_ApplicationsSerializer


class job_ApplicationsUpdate(RetrieveUpdateAPIView):
    queryset = job_Applications.objects.all()
    serializer_class = job_ApplicationsSerializer


class job_ApplicationsListPersonal(ListAPIView):
    serializer_class = job_ApplicationsSerializer

    def get_queryset(self):
        return job_Applications.objects.filter(
            is_available=True, profile=self.kwargs.get("profile")
        )


class MyApplicationList(ListAPIView):
    serializer_class = MyJobsListSerializer

    def get_queryset(self):
        return job_Applications.objects.filter(
            is_available=True, job_post=self.kwargs.get("job_post")
        )


class MySingleJobsList(RetrieveAPIView):
    queryset = job_Applications.objects.filter(is_available=True)
    serializer_class = MyJobsListSerializer


class MySingleJobsListRead(ListAPIView):
    serializer_class = MyJobsListSerializer

    def get_queryset(self):
        return job_Applications.objects.filter(
            Read=True, is_available=True, job_post=self.kwargs.get("job_post")
        )


class MySingleJobsListUnRead(ListAPIView):
    serializer_class = MyJobsListSerializer

    def get_queryset(self):
        return job_Applications.objects.filter(
            Read=False, is_available=True, job_post=self.kwargs.get("job_post")
        )



class MySingleJobsAccepted(ListAPIView):
    serializer_class = MyJobsListSerializer
    def get_queryset(self):
        return job_Applications.objects.filter(
            ApplicationStatus ='Accept', is_available=True, job_post=self.kwargs.get("job_post")
        )


class MyJobsList(ListAPIView):
    serializer_class = MyJobsListSerializer

    def get_queryset(self):
        return job_Applications.objects.filter(
            is_available=True, profile=self.kwargs.get("profile")
        )


class ReportJobPostAdd(ListCreateAPIView):
    queryset = ReportJobPost.objects.all()
    serializer_class = ReportJobPostSerializer


class ReportJobPostList(ListCreateAPIView):
    queryset = ReportJobPost.objects.all()
    serializer_class = ReportJobPostListSerializer


def test(request):
    test_func.delay()
    return HttpResponse("Done")
