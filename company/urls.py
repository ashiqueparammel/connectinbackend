from django.urls import path
from . import views

urlpatterns = [
    path('companyadd/',views.CompanyAdd.as_view(), name='CompanyAdd'),
    path('companyupdate/<int:pk>/',views.CompanyUpdate.as_view(), name='CompanyUpdate'),
    
    path('jobadd/',views.JobAdd.as_view(), name='JobAdd'),
    path('joblist/<int:company_id>/',views.JobList.as_view(), name='JobList'),
    path('jobupdate/<int:pk>/',views.JobUpdate.as_view(), name='JobUpdate'),   
    
    path('companydetails/<int:user_id>/',views.CompanyDetail.as_view(), name='CompanyDetail'),   
    path('joblistuser/',views.JobListUser.as_view(), name='JobListUser'),   
    path('jobuserview/<int:pk>/',views.JobUserView.as_view(), name='JobUserView'),   
    
]