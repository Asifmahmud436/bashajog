from rest_framework import serializers
from .models import Owner
from django.contrib.auth import get_user_model

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','username','first_name','last_name','email','user_type']

class OwnerSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    class Meta:
        model = Owner
        fields = '__all__'

class OwnerRegistrationSerializer(serializers.ModelSerializer):
    phone_no = serializers.IntegerField()
    confirm_password = serializers.CharField(max_length=50,required=True)

    class Meta:
        model = User
        fields = ['username','first_name','last_name','phone_no','email','password','confirm_password']

    def save(self):
        username = self.validated_data['username']
        first_name = self.validated_data['first_name']
        last_name = self.validated_data['last_name']
        phone_no = self.validated_data['phone_no']
        email = self.validated_data['email']
        password = self.validated_data['password']
        confirm_password = self.validated_data['confirm_password']

        if password!=confirm_password:
            raise serializers.ValidationError({'error':"Password doesnt match"})

        if User.objects.filter(email=email,user_type='Owner').exists():
            raise serializers.ValidationError({"error":"User with the email already exists!"})

        account = User(
            username=username,
            first_name=first_name,
            last_name=last_name,
            email=email,
            user_type='Owner',
        )

        account.set_password(password)
        account.is_active = False
        account.save()
        owner_account = Owner(
            user = account,
            phone_no = phone_no,
        )

        owner_account.save()
        return account
