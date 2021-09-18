import jwt
import environ

from django.contrib import auth

from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView

from .serializers import RegisterSerializer, LoginSerializer

env = environ.Env()


class RegisterView(GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request):
        """ Register a user in the api. """
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'status': True,
                'message': 'User registration successfully.',
                'data': serializer.data
            }, status=status.HTTP_201_CREATED)
        return Response({
            'status': False,
            'message': 'User registration failed.',
            'error': serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)


class LoginView(GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request):
        data = request.data
        username = data.get('username', '')
        password = data.get('password', '')
        user = auth.authenticate(username=username, password=password)

        if user:
            auth_token = jwt.encode({'username': user.username}, env('JWT_SECRET_KEY'))
            serializer = LoginSerializer(user)
            data = {'user': serializer.data, 'token': auth_token}
            return Response({
                'status': True,
                'message': 'Authentication success.',
                'data': data
            }, status=status.HTTP_200_OK)
        return Response({'status': False, 'message': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)


