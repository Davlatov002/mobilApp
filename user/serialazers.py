from rest_framework import serializers
from .models import Profile, Transaction

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'

class ProfilesingupSerialazer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['username', 'email', 'password','mac_address']

class Tranzaktionserialazer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ['username', 'balance_usdt','balance_netbo','balance_btc', 'created_at']

class ProfileRefeleshSerialazer(serializers.Serializer):
    referal_link = serializers.CharField()

class ProfileLoginserialazer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

class VerificationCodeserialazer(serializers.Serializer):
    code = serializers.CharField()
    
class UpdatePasswordSerializer(serializers.Serializer):
    password = serializers.CharField()

class UpdateProfileserialazer(serializers.Serializer):
    username=serializers.CharField()
    name=serializers.CharField()
    surname=serializers.CharField()
    profile_image=serializers.CharField()

# class UpdateProfileserialazer(serializers.ModelSerializer):
#     class Meta:
#         model = Profile
#         fields = ['email','password','username','name','surname','profile_image']

#     def update(self, instance, validated_data):
#         instance.email = validated_data.get("email", instance.email)
#         instance.password = validated_data.get("password", instance.password)
#         instance.username = validated_data.get("username", instance.username)
#         instance.name = validated_data.get("name", instance.name)
#         instance.surname = validated_data.get("surname", instance.surname)
#         instance.profile_image = validated_data.get("profile_image", instance.profile_image)

class GMProfileserialazer(serializers.Serializer):
    email = serializers.EmailField()
