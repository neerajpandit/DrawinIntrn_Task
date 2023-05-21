from rest_framework import serializers
from .models import User
from rest_framework.validators import UniqueTogetherValidator

class UserSerializer(serializers.ModelSerializer):
     class Meta:
         model = User
         fields = '__all__'
         validators = [
            UniqueTogetherValidator(
                queryset=User.objects.all(),
                fields=['email']
            )
        ]

    # username = serializers.CharField(max_length=100)
    # password = serializers.CharField(max_length=100)
    # mobile = serializers.CharField(max_length=10)
    # name = serializers.CharField(max_length=100)
    # address = serializers.CharField(max_length=100)
    # email = serializers.EmailField(validators=[UniqueValidator(queryset=User.objects.all())])