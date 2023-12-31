from django.urls import path
from . import views
from rest_framework_simplejwt import views as jwt_views
urlpatterns = [
    path('signup/',views.Signup.as_view(), name='sign_up'),
    path('verify/<str:uidb64>/<str:token>/', views.VerifyUserView.as_view(), name='verify-user'),
    path('token/',views.MyTokenObtainPairView.as_view(), name='MyTokenObtainPairView'),
    path('google_signup/',views.Google_Signup.as_view(), name='Google_Signup'),
    path('google_login/',views.Google_login.as_view(), name='Google_login'),
    path('userlist/',views.UserList.as_view(), name='UserList'),
    path('companylist/',views.CompanyList.as_view(), name='CompanyList'),
    path('commonskillsadd/',views.CommonSkillsAdd.as_view(), name='CommonSkillsAdd'),
    path('Userdetails/<int:pk>/',views.UserDetails.as_view(), name='UserDetails'),
    path('companydetails/<int:pk>/',views.CompanyDetails.as_view(), name='CompanyDetails'),
    path('commonskillsupdate/<int:pk>/',views.CommonSkillsUpdate.as_view(), name='CommonSkillsUpdate'),  
    path('authentication/',views.Authentication.as_view(), name='Authentication'), 
    path('logout/',views.logout.as_view(), name='logout'), 
    path('token/refresh/',jwt_views.TokenRefreshView.as_view(),name ='token_refresh'),
    path('refreshtoken/',views.RefreshTokenAuto.as_view(),name ='RefreshTokenAuto'),
    path('publicpostadd/',views.PublicPostAdd.as_view(),name ='PublicPostAdd'),
    path('publicpostlist/',views.PublicPostList.as_view(),name ='PublicPostList'),
    path('publicpostupdate/<int:pk>/',views.PublicPostUpdate.as_view(),name ='PublicPostUpdate'),
    path('addlikes/',views.AddLikes.as_view(),name ='AddLikes'),
    path('updatelikes/<int:pk>/',views.UpdateLikes.as_view(),name ='UpdateLikes'),
    path('addcomments/',views.AddComments.as_view(),name ='AddComments'),
    path('updatecomments/<int:pk>/',views.UpdateComments.as_view(),name ='UpdateComments'),
    path('notinterestedposts/',views.NotInterestedPosts.as_view(),name ='NotInterestedPosts'),
    path('publicpostreport/',views.PublicPostReport.as_view(),name ='PublicPostReport'),
    path('usersearchlist/',views.UserSearchList.as_view(),name ='UserSearchList'),
     
]