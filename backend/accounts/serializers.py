from rest_framework import serializers
from .models import MyModel
from django.contrib.auth.models import User



class MySerializer(serializers.ModelSerializer):
    class Meta:
        model = MyModel
        fields = '__all__'


from rest_framework import serializers


class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        user = User.objects.create_user(
            validated_data['username'],
            validated_data['email'],
            validated_data['password']
        )
        return user
    

