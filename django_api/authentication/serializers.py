from django.contrib.auth import get_user_model

from rest_framework import serializers

# Get the table user from db
User = get_user_model()


class RegisterSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(max_length=255, min_length=2)
    last_name = serializers.CharField(max_length=255, min_length=2)
    email = serializers.EmailField(max_length=255, min_length=5)
    password = serializers.CharField(max_length=65, min_length=8, write_only=True)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password']

    def validate(self, attrs):
        email = attrs.get('email', '')
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError({
                'status': False,
                'email': 'Email is already in use.'
            })
        return super().validate(attrs)
    
    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=100, min_length=2)
    password = serializers.CharField(max_length=65, min_length=8, write_only=True)
