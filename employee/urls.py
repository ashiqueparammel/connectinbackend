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
]
