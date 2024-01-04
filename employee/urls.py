from django.urls import path
from . import views

urlpatterns = [
    path('employeeprofileadd/',views.EmployeeProfileAdd.as_view(), name='EmployeeProfileAdd'),
    path('savepostadd/',views.SavePostAdd.as_view(), name='SavePostAdd'),
    path('educationadd/',views.EducationAdd.as_view(), name='EducationAdd'),
    path('personalskillsadd/',views.PersonalSkillsAdd.as_view(), name='PersonalSkillsAdd'),
    path('jobapplicationsadd/',views.job_ApplicationsAdd.as_view(), name='job_ApplicationsAdd'),
    path('employeeprofileupdate/<int:pk>/',views.EmployeeProfileUpdate.as_view(), name='EmployeeProfileUpdate'),
    path('savepostupdate/<int:pk>/',views.SavePostUpdate.as_view(), name='SavePostUpdate'),   
    path('educationupdate/<int:pk>/',views.EducationUpdate.as_view(), name='EducationUpdate'),   
    path('personalskillsupdate/<int:pk>/',views.PersonalSkillsUpdate.as_view(), name='PersonalSkillsUpdate'),   
    path('jobapplicationsupdate/<int:pk>/',views.job_ApplicationsUpdate.as_view(), name='job_ApplicationsUpdate'),   
    path('userprofiledetails/<int:user>/',views.EmployeeProfileDetail.as_view(), name='EmployeeProfileDetail'),   
    path('usersavepostdetail/<int:user>/',views.UserSavePostDetail.as_view(), name='UserSavePostDetail'),
    path('listPersonalSkills/<int:profile>/', views.ListPersonalSkills.as_view(), name='ListPersonalSkills'),
    path('removePersonalSkills/<int:pk>/', views.RemovePersonalSkills.as_view(), name='RemovePersonalSkills'),
    path('listPersonalEducation/<int:profile>/', views.ListPersonalEducation.as_view(), name='ListPersonalEducation'),
    path('jobapplicationslistpersonal/<int:profile>/', views.job_ApplicationsListPersonal.as_view(), name='job_ApplicationsListPersonal'),
    path('myjobslist/<int:profile>/', views.MyJobsList.as_view(), name='MyJobsList'),
    path('mysinglejobslist/<int:pk>/', views.MySingleJobsList.as_view(), name='MySingleJobsList'),
    path('mysinglejobslistunread/<int:job_post>/', views.MySingleJobsListUnRead.as_view(), name='MySingleJobsListUnRead'),
    path('mysinglejobslistread/<int:job_post>/', views.MySingleJobsListRead.as_view(), name='MySingleJobsListRead'),
    path('myapplicationlist/<int:job_post>/', views.MyApplicationList.as_view(), name='MyApplicationList'),
    path('reportjobpostadd/', views.ReportJobPostAdd.as_view(), name='ReportJobPostAdd'),
    path('reportjobpostlist/', views.ReportJobPostList.as_view(), name='ReportJobPostList'),
]
