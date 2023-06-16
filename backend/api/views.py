from api.models import User, File, Data
from api.serializers import FileSerializer, DataSerializer
from rest_framework.permissions import AllowAny
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework import generics
from django.http import JsonResponse
from rest_framework.authentication import TokenAuthentication
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK
)

@api_view(('POST',))
@permission_classes([AllowAny])
def api_get_token(request, *args, **kwargs):
    email = request.data['email']
    password = request.data.get('password')
    if email is None or password is None:
        return JsonResponse({'error': 'Please provide both username and password!'}, status=HTTP_400_BAD_REQUEST)
    if not email:
        return JsonResponse({'error': 'Invalid credentials!'}, status=HTTP_404_NOT_FOUND)
    userobject = User.objects.filter(email=email)
    user = userobject[0]

    if(userobject):
        token, created = Token.objects.get_or_create(
            user=userobject[0])  # Create token for the user
        if(user.check_password(password)):
            return JsonResponse({'status': 'ok', 'token': token.key}, status=HTTP_200_OK)
        else:
            return JsonResponse({'status': 'Wrong Password!', 'token': ''}, status=HTTP_400_BAD_REQUEST)
    else:
        return JsonResponse({'status': 'fail', 'response': 'user could not be found!'})

@api_view(('POST',))
@permission_classes([AllowAny])
def api_register_view(request, *args, **kwargs):
    data = request.data
    user = User(email=data['email'], username=data['username'])
    user.set_password(data['password'])
    user.save()
    if user.pk is not None:
        return JsonResponse({'status': 'ok', 'response': 'The account is created!'}, status=HTTP_200_OK)

class FileList(generics.ListCreateAPIView):
    authentication_classes = [TokenAuthentication]
    queryset = File.objects.all()
    serializer_class = FileSerializer

class FileDetail(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [TokenAuthentication]
    queryset = File.objects.all()
    serializer_class = FileSerializer

class DataList(generics.ListCreateAPIView):
    authentication_classes = [TokenAuthentication]
    queryset = Data.objects.all()
    serializer_class = DataSerializer

class DataDetail(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [TokenAuthentication]
    queryset = Data.objects.all()
    serializer_class = DataSerializer