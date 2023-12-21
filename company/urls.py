from django.urls import path
from . import views

urlpatterns = [
    path('companyadd/',views.CompanyAdd.as_view(), name='CompanyAdd'),
    path('companyupdate/<int:pk>/',views.CompanyUpdate.as_view(), name='CompanyUpdate'),
    
    path('jobadd/',views.JobAdd.as_view(), name='JobAdd'),
    path('joblist/<int:company>/',views.JobList.as_view(), name='JobList'),
    path('jobupdate/<int:pk>/',views.JobUpdate.as_view(), name='JobUpdate'),   
    
    path('companydetails/<int:user>/',views.CompanyDetail.as_view(), name='CompanyDetail'),   
    path('joblistuser/',views.JobListUser.as_view(), name='JobListUser'),   
    path('jobskillsadd/',views.JobRequired_Skills.as_view(), name='JobRequired_Skills'),   
    path('jobuserview/<int:pk>/',views.JobUserView.as_view(), name='JobUserView'),   
    path('listrequiredskills/<int:job>/',views.ListRequired_Skills.as_view(), name='ListRequired_Skills'),   
    path('updatejobskills/<int:pk>/',views.RemoveJobRequired_Skills.as_view(), name='RemoveJobRequired_Skills'),   
    
]