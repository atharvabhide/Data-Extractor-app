from api.models import File
from rest_framework.serializers import ModelSerializer
from rest_framework.serializers import ValidationError

class FileSerializer(ModelSerializer):
    class Meta:
        model = File
        exclude = ['user']

    def create(self, validated_data):
        user = self.context['request'].user
        file = File.objects.create(user=user, **validated_data)
        return file
    
    def validate(self, attrs):
        if (attrs['file'] == None):
            raise ValidationError("File is required")
        return attrs