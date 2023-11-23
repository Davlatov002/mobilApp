from rest_framework import serializers
from .models import Profile

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'

class ProfilesingupSerialazer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['username', 'email', 'password']

class ProfileRefeleshSerialazer(serializers.Serializer):
    referal_link = serializers.UUIDField()

class ProfileLoginserialazer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)



class UpdateProfileserialazer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['email','password','username','name','surname','profile_image','referal_link']

    def update(self, instance, validated_data):
        instance.email = validated_data.get("email", instance.email)
        instance.password = validated_data.get("password", instance.password)
        instance.username = validated_data.get("username", instance.username)
        instance.name = validated_data.get("name", instance.name)
        instance.surname = validated_data.get("surname", instance.surname)
        instance.profile_image = validated_data.get("profile_image", instance.profile_image)
        instance.referal_link = validated_data.get("referal_link", instance.referal_link)

class PrsswProfileserialazer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['password']

    def update(self, instance, validated_data):
        instance.password = validated_data.get("password", instance.password)