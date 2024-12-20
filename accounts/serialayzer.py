from rest_framework import serializers
from NurCRM.models import CustomUser
from django.contrib.auth import authenticate


from django.contrib.auth.hashers import make_password

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, style={'input_type': 'password'})
    password_confirm = serializers.CharField(write_only=True, required=True, style={'input_type': 'password'})

    class Meta:
        model = CustomUser
        fields = ['username', 'email','phone_number','password', 'password_confirm']

    def validate(self, data):
        # Тасдиқ кардани мувофиқати паролҳо
        if data['password'] != data['password_confirm']:
            raise serializers.ValidationError({"password": "Passwords do not match."})
        return data

    def create(self, validated_data):
        # Майдони `password_confirm`-ро хориҷ мекунем
        validated_data.pop('password_confirm')
        
        # Ҳаши паролро пеш аз сабт кардан месозем
        validated_data['password'] = make_password(validated_data['password'])

        # Объекти корбарро эҷод мекунем
        return CustomUser.objects.create(**validated_data)




class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True, style={'input_type': 'password'})

    def validate(self, data):
        user = authenticate(username=data['username'], password=data['password'])
        if not user:
            raise serializers.ValidationError({"detail": "Invalid username or password"})
        return user
    

