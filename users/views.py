import requests
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import CommonSkills, CustomUser
from .serializers import CommonSkillsSerializer, User_Sign_Up, myTokenObtainPairSerializer, userDataSerializer
from django.template.loader import render_to_string
from django.core.mail import send_mail
from django.utils.encoding import force_str, force_bytes
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.urls import reverse
from django.contrib.auth.tokens import default_token_generator
from rest_framework.generics import GenericAPIView, ListAPIView, UpdateAPIView,ListCreateAPIView,RetrieveUpdateAPIView
from django.http import HttpResponseRedirect
from decouple import config
from rest_framework.filters import SearchFilter
from rest_framework_simplejwt.tokens import RefreshToken
from django.core.validators import validate_email
from django.core.exceptions import ValidationError

class Signup(APIView):
    template_name = "activation/activation_email.html"
     
    def post(self, request):
        serializer = User_Sign_Up(data=request.data)
        data = request.data
        if serializer.is_valid():
            user = serializer.save()
            token = default_token_generator.make_token(
                user
            )  # Create a verification token
            uid = urlsafe_base64_encode(force_bytes(user.pk))
            verification_url = reverse(
                "verify-user", kwargs={"uidb64": uid, "token": token}
            )  # Construct the verification URL
            context = {
                "user": user,
                "verification_url": request.build_absolute_uri(
                    verification_url
                ),  # Render the HTML content of the email
            }
            email_html_message = render_to_string(
                "activation/activation_email.html", context
            )
            # Send the verification email
            subject = "Connect in | Activate Your Account"
            from_email = "cootinternational@gmail.com"
            recipient_list = [user.email]

            send_mail(
                subject,
                email_html_message,
                from_email,
                recipient_list,
                html_message=email_html_message,
                fail_silently=True,
            )

            # print(is_sent,'------------> is sent')
            data = {"Text": "registered", "status": 200}
            return Response(data=data)
        else:
            statusText = serializer.errors
            data = {"Text": statusText, "status": 404}
            return Response(data=data)
        
    
        

class VerifyUserView(GenericAPIView):
    def get(self, request, uidb64, token):
        try:
            uid = force_str(urlsafe_base64_decode(uidb64))
            user = CustomUser.objects.get(pk=uid)
            if default_token_generator.check_token(user, token):
                user.is_active = True
                user.save()
                message = "Congrats! Account activated!"
                url = config("front_end_url")
                redirect_url = f"{url}login" + "?message=" + message
                return HttpResponseRedirect(redirect_url)
            else:
                message = "Activation Link expired, please register again."
                url = config("front_end_url")
                redirect_url = f"{url}signup" + "?message=" + message
                return HttpResponseRedirect(redirect_url)
        except Exception as e:
            message = "Activation Link expired, please register again."
            url = config("front_end_url")
            redirect_url = f"{url}signup" + "?message=" + message
            return HttpResponseRedirect(redirect_url)


class Google_Signup(APIView):
    
    def post(self, request):
        
        email = request.data.get("email")
        is_company = request.data.get("is_company")

        if not CustomUser.objects.filter(email=email).exists():
            if is_company == "":
                data = {
                    "Text": "Your not Signed Please signup !",
                    "status": 204,
                }
                return Response(data=data)
            serializer = User_Sign_Up(data=request.data)
            if serializer.is_valid():
                user = serializer.save()
                user.save()
                data = {
                    "Text": "Your google SignUp successfully!",
                    "signup": "signup",
                    "status": 200,
                }
                return Response(data=data)
        if CustomUser.objects.filter(email=email).exists():
            data = {
                "Text": "This Email alredy exist!",
                "status": 403,
            }
            return Response(data=data)
        
        else:
            data = {"Text": serializer.errors, "status": 404}
            return Response(data=data)
        
class Google_login (APIView):
    
    def post(self, request):
        
        email = request.data.get("email")
        
        if CustomUser.objects.filter(email=email).exists(): 
            access_token = request.data.get("access_token")
            Googleurl = config("GOOGLE_VERYFY")
            get_data = f"{Googleurl}access_token={access_token}"
            response = requests.get(get_data)

            if response.status_code == 200:
                user_data = response.json()
                check_email = user_data['email']
                if check_email == email:
                    user = CustomUser.objects.get(email=email)
                    token = RefreshToken.for_user(user)
                    token["email"] = user.email
                    token["is_active"] = user.is_active
                    token["is_superuser"] = user.is_superuser
                    token["is_company"] = user.is_company
                    token["is_google"] = user.is_google
                    dataa = {
                        "refresh": str(token),
                        "access": str(token.access_token),
                    }
                    
                    if user.is_active:
                        data = {
                        "message": "Your Login successfully! ",
                        "status": 201,
                        "token": dataa,
                    }
                    else:
                         data = {
                        "message": "Your Account has been blocked ! ",
                        "status": 202,
                        "token": dataa,
                    }
                            
                    return Response(data=data)   
            else:
                data = {
                    "message": response.text,
                    "status": 406,
                }
                return Response(data=data)  
        else:
            data = {
                        "message": "This Email have no account please Create new account! ",
                        "status": 403,
                    }
            return Response(data=data)     

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = myTokenObtainPairSerializer


class UserList(ListAPIView):
    queryset = CustomUser.objects.filter(is_superuser=False,is_company=False)
    filter_backends = (SearchFilter,)
    search_fields = ("username", "email","id","is_active","phone_number")
    serializer_class = userDataSerializer


class UserDetails(RetrieveUpdateAPIView):
    queryset = CustomUser.objects.filter(is_superuser=False, is_company=False)
    serializer_class = userDataSerializer


class CompanyList(ListAPIView):
    queryset = CustomUser.objects.filter(is_superuser=False, is_company=True)
    filter_backends = (SearchFilter,)
    search_fields = ("username", "email","id","is_active", "phone_number")
    serializer_class = userDataSerializer


class CompanyDetails(RetrieveUpdateAPIView):
    queryset = CustomUser.objects.filter(is_superuser=False, is_company=True)
    serializer_class = userDataSerializer
    

class CommonSkillsAdd(ListCreateAPIView):
    queryset =  CommonSkills.objects.all()
    filter_backends = (SearchFilter,)
    search_fields = ('__all__')
    serializer_class = CommonSkillsSerializer    
    
class CommonSkillsUpdate(RetrieveUpdateAPIView):
    queryset =  CommonSkills.objects.all()
    serializer_class = CommonSkillsSerializer       
           
       
