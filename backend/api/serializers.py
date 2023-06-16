from api.models import File, Data
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

class DataSerializer(ModelSerializer):
    class Meta:
        model = Data
        exclude = ['user', 'file']

    def create(self, validated_data):
        user = self.context['request'].user
        data = Data.objects.create(user=user, **validated_data)
        return data
    
    def validate(self, attrs):
        if 'uuid' not in attrs:
            raise ValidationError("UUID is required")
        if (attrs['data'] == None):
            raise ValidationError("Data is required")
        file = File.objects.get(uuid=attrs['uuid'])
        if (file == None):
            raise ValidationError("File not found")
        print(attrs)
        attrs.pop('uuid')
        attrs['file'] = file
        return attrs