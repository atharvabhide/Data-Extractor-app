from api.models import File, User
from rest_framework.serializers import ModelSerializer
from rest_framework.serializers import ValidationError

class FileSerializer(ModelSerializer):
    class Meta:
        model = File
        exclude = ['uuid', 'user']

    def create(self, validated_data):
        email = self.context['request'].data['email']
        user = User.objects.get(email=email)
        file = File.objects.create(user=user, **validated_data)
        return file
    
    def validate(self, attrs):
        if (attrs['file'] == None):
            raise ValidationError("File is required")
        return attrs
    