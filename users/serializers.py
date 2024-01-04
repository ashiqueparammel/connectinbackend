from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from .models import Comments, CommonSkills, CustomUser, Like, NotInterestedPost, PublicPost, ReportPublicPost


class User_Sign_Up(ModelSerializer):
    password2 = serializers.CharField(
        style={"input_type": "passsword"}, write_only=True
    )

    class Meta:
        model = CustomUser
        fields = "__all__"

    def save(self):
        user = CustomUser(
            username=self._validated_data["username"],
            email=self._validated_data["email"],
            phone_number=self._validated_data["phone_number"],
            password=self._validated_data["password"],
            is_active=False,
        )
        password = self._validated_data["password"]
        password2 = self._validated_data["password2"]
        if password != password2:
            raise serializers.ValidationError({"password": "password does not match"})
        user.set_password(password)
        if self._validated_data["is_company"] is True:
            user.is_company = True
        if self._validated_data["is_google"] is True:
            user.is_google = True
            user.is_active = True
        user.save()
        return user


class myTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token["email"] = user.email
        token["is_active"] = user.is_active
        token["is_superuser"] = user.is_superuser
        token["is_company"] = user.is_company
        token["is_google"] = user.is_google
        return token


class userDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = [
            "id",
            "username",
            "email",
            "is_superuser",
            "is_company",
            "phone_number",
            "profile_cover_image",
            "is_active",
            "profile_image",
        ]


class CommonSkillsSerializer(ModelSerializer):
    class Meta:
        model = CommonSkills
        fields = "__all__"


class PublicPostAddSerializer(ModelSerializer):
    class Meta:
        model = PublicPost
        fields = "__all__"


class PublicPostListSerializer(ModelSerializer):
    user = userDataSerializer()

    class Meta:
        model = PublicPost
        fields = "__all__"


class LikeSerializer(ModelSerializer):
    class Meta:
        model = Like
        fields = "__all__"


class CommentsSerializer(ModelSerializer):
    class Meta:
        model = Comments
        fields = "__all__"


class NotInterestedPostsSerializer(ModelSerializer):
    class Meta:
        model = NotInterestedPost
        fields = "__all__"

class ReportPublicPostSerializer(ModelSerializer):
    class Meta:
        model = ReportPublicPost
        fields = "__all__"