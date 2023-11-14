from django.urls import path
from . import views

urlpatterns = [
    path('signup/',views.Signup.as_view(), name='sign_up'),
    path('google_signup/',views.Google_Signup.as_view(), name='Google_Signup'),
    path('verify/<str:uidb64>/<str:token>/', views.VerifyUserView.as_view(), name='verify-user'),
    path('token/',views.MyTokenObtainPairView.as_view(), name='MyTokenObtainPairView'),
    
]