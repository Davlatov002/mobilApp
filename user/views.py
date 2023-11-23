from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Profile
from drf_yasg.utils import swagger_auto_schema
from .serialazers import ProfileSerializer, ProfilesingupSerialazer, ProfileLoginserialazer, UpdateProfileserialazer, ProfileRefeleshSerialazer,PrsswProfileserialazer
from datetime import date
import random

# gmail######
# import smtp
# #####

# @swagger_auto_schema(method='PATCH', operation_description="Tiklamoqchi bo'lgan profilning ID sini kirting!")
# @api_view(['PATCH'])
# def confirmation(request, username):
#     if request.method == 'PATCH':
#         try:
#             profile = Profile.objects.get(username=username)
#         except:
#             return Response({'error': 'Username mavjud emas!'}, status=status.HTTP_400_BAD_REQUEST)
#         six_digit_number = str(random.randint(100000, 999999))
#         gmail = str(profile.email)
#         send_email("Verification code",f'{  six_digit_number  }', gmail)
#         profile == six_digit_number
#         profile.save()
#         return Response({'messege': 'Xabar yuborildi!'},status=status.HTTP_200_OK)
#     else:
#         return Response({'messege': 'Error'},status=status.HTTP_400_BAD_REQUEST)
    
# @swagger_auto_schema(method='PATCH', operation_description="Tiklamoqchi bo'lgan profilning ID sini kirting!")
# @api_view(['PATCH'])
# def verification_code(request, v_code):
#     if request.method == 'PATCH':
#         try:
#             profile = Profile.objects.get(verification_code=v_code)
#         except:
#             return Response({'error': 'Username mavjud emas!'}, status=status.HTTP_400_BAD_REQUEST)
#         profile.
        

@swagger_auto_schema(method='POST', request_body=ProfilesingupSerialazer, operation_description="Malumotlarni kirting")
@api_view(['POST'])
def signup(request):
    profiles = Profile.objects.all()
    usernames = [profile.username for profile in profiles]
    username = request.data.get('username')
    email = request.data.get('email')
    gm = [profile.email for profile in profiles]
    serializer = ProfileSerializer(data=request.data)
    if username in usernames:
        return Response({'message': 'This username exists!'}, status=status.HTTP_400_BAD_REQUEST)
    elif email in gm:
        return Response({'message': 'This email exists!'}, status=status.HTTP_400_BAD_REQUEST)
    elif serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        return Response({'error': 'Registration failed!'}, status=status.HTTP_400_BAD_REQUEST)

@swagger_auto_schema(methods='GET')
@api_view(['GET'])
def get_profil(request):
    if request.method == 'GET':
        profile = Profile.objects.all()
        serializer = ProfileSerializer(profile, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        return Response({'messege': 'Error'},status=status.HTTP_400_BAD_REQUEST)

@swagger_auto_schema(methods='GET')
@api_view(['GET'])
def get_profil_pk(request, pk):
    if request.method == 'GET':
        profile = Profile.objects.get(id=pk)
        serializer = ProfileSerializer(profile)
        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        return Response({'messege': 'Error'},status=status.HTTP_400_BAD_REQUEST)
    
@swagger_auto_schema(method='POST', request_body=ProfileLoginserialazer, operation_description="Malumotlarni kirting")
@api_view(['POST'])
def login_view(request):
    username = request.data.get('username')
    password = request.data.get('password')
    try:
        profile = Profile.objects.get(username=username)
    except:
        return Response({'error': 'Username does not exist!'}, status=status.HTTP_400_BAD_REQUEST)
    if profile:
        if profile.password == password:
            profile_serializer = ProfileSerializer(profile)
            return Response({'profile': profile_serializer.data, 'message': 'Login successful!'}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Password failed error!'}, status=status.HTTP_400_BAD_REQUEST)
    return Response({'error': 'Username does not exist!'}, status=status.HTTP_400_BAD_REQUEST)



@swagger_auto_schema(method='PATCH', request_body=UpdateProfileserialazer, operation_description="Yangilamaoqchi bo'lgan Profilening ID sini kirting")
@api_view(['PATCH'])
def profile_update(request, pk):
    profile = Profile.objects.get(id=pk)        
    data = ProfileSerializer(instance=profile, data=request.data)
    if data.is_valid():
        data.save()
        return Response(data.data, status=status.HTTP_200_OK)
    else:
        return Response({'messege': 'Error'},status=status.HTTP_400_BAD_REQUEST)
    

@swagger_auto_schema(method='DELETE', operation_description="O'chirmoqchi bo'lgan Profileni ID sini kirting")
@api_view(['DELETE'])
def delete_later(request, pk):
    if request.method == 'DELETE':
        praduct = Profile.objects.get(id=pk)
        data = ProfileSerializer(praduct)
        praduct.is_archived = date.today()
        praduct.save()
        return Response(data.data, status=status.HTTP_200_OK)
    else:
        return Response({'massage':"Deleted error"}, status=status.HTTP_400_BAD_REQUEST)
    
@swagger_auto_schema(method='DELETE', operation_description="O'chirmoqchi bo'lgan Profileni ID sini kirting")
@api_view(['DELETE'])
def profile_delete(request, pk):
    if request.method == 'DELETE':
        praduct = Profile.objects.get(id=pk)
        praduct.delete()
        return Response({'massage':"Deleted successfully"},status=status.HTTP_200_OK)
    else:
        return Response({'massage':"Deleted error"},status=status.HTTP_400_BAD_REQUEST)
    
@swagger_auto_schema(method='PATCH', request_body=ProfileRefeleshSerialazer, operation_description="Referal_link")
@api_view(['PATCH'])
def referal_link(request, pk):
    if request.method == 'PATCH':
        referal = request.data.get('referal_link')
        try:
            frend = Profile.objects.get(referal_link=referal)
        except:
            return Response({'error': 'No such referl_link exists!'}, status=status.HTTP_400_BAD_REQUEST)
        profile = Profile.objects.get(id=pk)
        profile.balance += 5
        profile.save()
        frend.balance += 5
        frend.save()
        return Response({'messege': 'Ok!'}, status=status.HTTP_200_OK)
    else:
        return Response({'messege': 'Error'},status=status.HTTP_400_BAD_REQUEST)
    
@swagger_auto_schema(method='PATCH', operation_description="Ball berladigan profile ID sini kirting")
@api_view(['PATCH'])
def ball(request, pk):
    if request.method == 'PATCH':
        profile = Profile.objects.get(id=pk)        
        profile.balance += 2
        profile.save()
        return Response({'messege': 'Ok!'},status=status.HTTP_200_OK)
    else:
        return Response({'messege': 'Error'},status=status.HTTP_400_BAD_REQUEST)