from rest_framework import serializers
from .models import Tenant
from django.contrib.auth import get_user_model

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email','user_type']
        ref_name = 'TenantUserSerializer'

class TenantSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    class Meta:
        model = Tenant
        fields = '__all__'

class TenantRegistrationSerializer(serializers.ModelSerializer):
    phone_no = serializers.IntegerField()
    confirm_password = serializers.CharField(max_length=20,required=True)

    class Meta:
        model = User
        fields = ['username','first_name','last_name','email','phone_no','password','confirm_password']
    def save(self):
        username = self.validated_data['username']
        first_name = self.validated_data['first_name']
        last_name = self.validated_data['last_name']
        email = self.validated_data['email']
        phone_no = self.validated_data['phone_no']
        password = self.validated_data['password']
        confirm_password = self.validated_data['confirm_password']

        if password!=confirm_password:
            raise serializers.ValidationError({"error":"Password does not match!"})

        if User.objects.filter(email=email,user_type='Tenant').exists():
            raise serializers.ValidationError({"error":"User with this email already exists!"})

        account = User(
            username=username,
            first_name=first_name,
            last_name=last_name,
            email=email,
            user_type = 'Tenant',
        )
        account.set_password(password)
        account.is_active = False
        account.save()

        tenant_account = Tenant(
            user = account,
            phone_no = phone_no,
            
        )
        tenant_account.save()
        return account