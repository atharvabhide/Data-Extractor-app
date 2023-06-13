from django.urls import path 
from api.views import FileList, FileDetail
from rest_framework.views import APIView
from rest_framework.response import Response

class HomeView(APIView):
    def get(self, request):
        return Response({
            "api/files/": "List all files",
            "api/files/<str:pk>/": "Retrieve/Update/Delete a file",
        })

urlpatterns = [
    path('', HomeView.as_view()),
    path('files/', FileList.as_view()),
    path('files/<str:pk>/', FileDetail.as_view()),
]