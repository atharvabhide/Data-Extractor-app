from django.urls import path 
from api.views import FileList, FileDetail, DataList, DataDetail, api_get_token, api_register_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

class HomeView(APIView):
    permission_classes = [AllowAny]
    def get(self, request):
        return Response({
            'register/': 'Register a new user',
            'auth/': 'Authenticate a user and get a token',
            "api/files/": "List all files",
            "api/files/<str:pk>/": "Retrieve/Update/Delete a file",
            "api/data/": "List all data",
            "api/data/<str:pk>/": "Retrieve/Update/Delete a data"
        })

urlpatterns = [
    path('', HomeView.as_view()),
    path('register/', api_register_view, name='register'),
    path('auth/', api_get_token, name='auth'),
    path('files/', FileList.as_view()),
    path('files/<str:pk>/', FileDetail.as_view()),
    path('data/', DataList.as_view()),
    path('data/<str:pk>/', DataDetail.as_view()),
]