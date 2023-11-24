from django.urls import path
from . import views

urlpatterns = [
    path('signup/',views.Signup.as_view(), name='sign_up'),
    path('verify/<str:uidb64>/<str:token>/', views.VerifyUserView.as_view(), name='verify-user'),
    path('token/',views.MyTokenObtainPairView.as_view(), name='MyTokenObtainPairView'),
    path('google_signup/',views.Google_Signup.as_view(), name='Google_Signup'),
    path('google_login/',views.Google_login.as_view(), name='Google_login'),
    path('userlist/',views.UserList.as_view(), name='UserList'),
    path('Userdetails/',views.UserDetails.as_view(), name='UserDetails'),
    path('companylist/',views.CompanyList.as_view(), name='CompanyList'),
    path('companydetails/',views.CompanyDetails.as_view(), name='CompanyDetails'),
    
]