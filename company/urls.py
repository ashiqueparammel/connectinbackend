from django.urls import path
from . import views

urlpatterns = [
    path('companyadd/',views.CompanyAdd.as_view(), name='CompanyAdd'),
    path('jobadd/',views.JobAdd.as_view(), name='JobAdd'),
    path('companyupdate/<int:pk>/',views.CompanyUpdate.as_view(), name='CompanyUpdate'),
    path('jobupdate/<int:pk>/',views.JobUpdate.as_view(), name='JobUpdate'),
    
]