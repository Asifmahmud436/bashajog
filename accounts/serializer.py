from .models import CustomUser
from rest_framework import serializers
from django.contrib.auth import get_user_model
from dj_rest_auth.registration.serializers import RegisterSerializer


User = get_user_model()
class CustomRegistrationSerializer(RegisterSerializer):
    user_type = serializers.ChoiceField(choices=[("Landlord","Landlord"),
        ("Tenant","Tenant"),])

    def get_cleaned_data(self):
        data = super().get_cleaned_data()
        data['user_type'] = self.validated_data.get('user_type','')
        return data
    
    def save(self,request):
        user = super().save(request)
        user.user_type = self.validated_data.get('user_type')
        user.save()
        return user


# write_only doesnt returns the password,which is good for security purposes
class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True,write_only=True)


class UserAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['username','first_name','last_name','email','user_type','is_staff']