from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import get_user_model,login,logout,authenticate
from rest_framework.permissions import AllowAny
from .serializer import LoginSerializer,UserAccountSerializer
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404

User = get_user_model()

class UserDetailView(APIView):
    permission_classes = [AllowAny]

    def get(self,request,format=None):
        user_id = request.query_params.get('user_id')

        if not user_id:
            return Response({'error':'User ID required'},status=status.HTTP_400_BAD_REQUEST)
        
        user = get_object_or_404(User,id=user_id)
        serialzier = UserAccountSerializer(user)
        return Response(serialzier.data,status=status.HTTP_200_OK)

class LoginAPIView(APIView):
    serializer_class = LoginSerializer

    def post(self, request):
        serialized_data = self.serializer_class(data = request.data)

        if serialized_data.is_valid():
            username = serialized_data.validated_data['username']
            password = serialized_data.validated_data['password']
            user = authenticate(username = username, password = password)
            
            try:
                user2 = User._default_manager.get(username=username)
            except(TypeError, ValueError, OverflowError, User.DoesNotExist):
                user2 = None

            if user2 is not None:
                if user2.is_active:
                    if user is not None:
                        token, _ = Token.objects.get_or_create(user=user)
                        login(request, user)
                        return Response({'token': token.key, 'user_id': user.id})
                    else:
                        return Response({'error': "Invalid password. Please try again."})
                else:
                    return Response(
                        {'error': "Your account is not activated. Please check your email for the activation link."}
                    )
            else:
                return Response(
                    {'error': "Invalid Username. Please try again."}
                )
        return Response(serialized_data.errors)
    
class LogoutAPIView(APIView):
    def get(self,request):
        logout(request)
        return Response("Logout successful.",status=status.HTTP_200_OK)
    

# for google auth
from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from allauth.socialaccount.providers.oauth2.client import OAuth2Client
from dj_rest_auth.registration.views import SocialLoginView
from rest_framework.response import Response
from rest_framework import status
from .models import CustomUser
from owners.models import Owner
from tenants.models import Tenant

class GoogleLoginView(SocialLoginView):
    adapter_class = GoogleOAuth2Adapter
    client_class = OAuth2Client
    callback_url = "your-callback-url"  # Replace with your frontend callback URL
    
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        if response.status_code == 200:
            user = self.user
            # Check if user_type is provided in request
            user_type = request.data.get('user_type')
            
            if user_type:
                user.user_type = user_type
                user.save()
                
                # Create corresponding Owner or Tenant profile
                if user_type == 'Owner':
                    Owner.objects.get_or_create(
                        user=user,
                        defaults={
                            'phone_no': request.data.get('phone_no')
                        }
                    )
                elif user_type == 'Tenant':
                    Tenant.objects.get_or_create(
                        user=user,
                        defaults={
                            'phone_no': request.data.get('phone_no'),
                            'profession': request.data.get('profession', '')
                        }
                    )
                    
            return Response({
                'token': response.data.get('token'),
                'user': {
                    'id': user.id,
                    'email': user.email,
                    'username': user.username,
                    'user_type': user.user_type
                }
            })
        return response