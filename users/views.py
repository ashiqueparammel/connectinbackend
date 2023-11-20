from urllib.parse import quote
import requests
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.views import APIView
from rest_framework.response import Response
from connectin.settings import STATIC_URL
from .models import CustomUser
from .serializers import User_Sign_Up, myTokenObtainPairSerializer
from django.template.loader import render_to_string
from django.core.mail import send_mail
from django.utils.encoding import force_str, force_bytes
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.urls import reverse
from django.contrib.auth.tokens import default_token_generator
from rest_framework.generics import GenericAPIView
from django.http import HttpResponseRedirect
from decouple import config


class Signup(APIView):
    template_name = "activation/activation_email.html"

    def post(self, request):
        serializer = User_Sign_Up(data=request.data)
        data = request.data
        print(data, "cheeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeekk")
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
            )
            data = {"Text": "registered", "status": 200}
            return Response(data=data)
        else:
            statusText = serializer.errors
            data = {"Text": statusText, "status": 404}
            print(data, "errrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrror")
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
        is_google = request.data.get("is_google")
        if not CustomUser.objects.filter(email=email).exists():
            serializer = User_Sign_Up(data=request.data)
            if serializer.is_valid():
                user = serializer.save()
                user.save()
                data = {"token": "Your google SignUp successfully!","signup":"signup", "status": 200}
        if CustomUser.objects.filter(email=email, is_google=True).exists():
            user = CustomUser.objects.get(email=email)
            data = {"token": "Your google Login successfully!","login":"login", "status": 200}

        elif CustomUser.objects.filter(email=email, is_google=False).exists():
            data = {"token": "Your Email Already Exist  ! ", "status": 201}
            return Response(data=data)

        if user is not None:
            return Response(data=data)
        else:
            data = {"Text": serializer.errors, "status": 400}
            return Response(data=data)


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = myTokenObtainPairSerializer
