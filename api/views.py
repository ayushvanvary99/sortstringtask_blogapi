from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import ResgisterSerializer , LoginSerializer
from rest_framework import status


class RegisterView(APIView):

    def post(self, request):
        try:
            data = request.data

            serializer = ResgisterSerializer(data = data)

            if not serializer.is_valid():
                return Response({
                    'data': serializer.errors,
                    'message': 'something went wrong'
                }, status=status.HTTP_400_BAD_REQUEST)

            serializer.save()

            return Response({
                'data': {},
                'message': 'your account is created'
            }, status=status.HTTP_201_CREATED)

        except Exception:
            return Response({
                'data': {},
                'message': 'something went wrong'
            }, status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):

    def post(self, request):
        try:
            data = request.data
            serializer = LoginSerializer(data = data)

            if not serializer.is_valid():
                return Response({
                    'data': serializer.errors,
                    'message': 'something went wrong'
                }, status=status.HTTP_400_BAD_REQUEST)

            response = serializer.get_jwt_token(serializer.data)

            return Response(response, status=status.HTTP_200_OK)



        except Exception:
            return Response({
                'data': {},
                'message': 'something went wrong'
            }, status=status.HTTP_400_BAD_REQUEST)
