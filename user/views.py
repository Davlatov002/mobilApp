from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Profile
from drf_yasg.utils import swagger_auto_schema
from .serialazers import ProfileSerializer, ProfilesingupSerialazer, ProfileLoginserialazer, UpdateProfileserialazer, ProfileRefeleshSerialazer,VerificationCodeserialazer ,GMProfileserialazer, UpdatePasswordSerializer
import time
import random

# gmail######
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

globals
code_lis = {}

def send_email(subject, body, to_email):
    # Gmail pochtangiz va parolingizni kiriting
    gmail_user = 'pythonN15Django@gmail.com'
    gmail_password = 'hqmwjojhkgufgjsj'

    # Xabar tayyorlash
    message = MIMEMultipart()
    message['From'] = gmail_user
    message['To'] = to_email
    message['Subject'] = subject

    # Xabarning matnini qo'shish
    message.attach(MIMEText(body, 'plain'))

    # SMTP serveriga ulanish
    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()
        server.login(gmail_user, gmail_password)

        # Xabarni yuborish
        server.sendmail(gmail_user, to_email, message.as_string())
#####

@swagger_auto_schema(method='PATCH', request_body=GMProfileserialazer, operation_description="Tiklamoqchi bo'lgan profilning ID sini kirting!")
@api_view(['PATCH'])
def send_otp(request):
    if request.method == 'PATCH':
        try:
            email = request.data.get("email")
            profile = Profile.objects.get(email=email)
        except:
            return Response({'error': -2 }, status=status.HTTP_400_BAD_REQUEST)
        six_digit_number = str(random.randint(100000, 999999))
        gmail = str(profile.email)
        send_email("Verification code",f'{  six_digit_number  }', gmail)
        code_lis[six_digit_number]=gmail
        return Response({'message': 1 },status=status.HTTP_200_OK)
    else:
        return Response({'message': -1 },status=status.HTTP_400_BAD_REQUEST)
        
@swagger_auto_schema(method='PATCH', request_body=VerificationCodeserialazer, operation_description="Tiklamoqchi bo'lgan profilning ID sini kirting!")
@api_view(['PATCH'])
def confirmation_otp(request):
    if request.method == 'PATCH':
        code = request.data.get("code")
        if code in code_lis.keys():
            del code_lis[code]
            return Response({'message': 1 }, status=status.HTTP_200_OK)
        else:
            return Response({'message': -2 },status=status.HTTP_400_BAD_REQUEST)

    else:
        return Response({'message': -1 },status=status.HTTP_400_BAD_REQUEST)
    
@swagger_auto_schema(method='PATCH', request_body=UpdatePasswordSerializer, operation_description="Parolni o'zgartirish uchun so'rov")
@api_view(['PATCH'])
def update_password(request, email):
    try:
        profile = Profile.objects.get(email=email)
    except Profile.DoesNotExist:
        return Response({'message': -2 }, status=status.HTTP_404_NOT_FOUND)
    serializer = UpdatePasswordSerializer(data=request.data)
    if serializer.is_valid():
        new_password = serializer.validated_data['password']
        profile.password = new_password
        profile.save()
        return Response({'message': 1 }, status=status.HTTP_200_OK)
    else:
        return Response({'message': -1}, status=status.HTTP_400_BAD_REQUEST)

@swagger_auto_schema(method='DELETE', operation_description="O'chirmoqchi bo'lgan Profileni ID sini kirting")
@api_view(['DELETE'])
def archive_account(request, pk):
    if request.method == 'DELETE':
        profile = Profile.objects.get(id=pk)
        is_data = int(time.time())
        profile.is_archived = is_data
        profile.save()
        return Response({'message': 1}, status=status.HTTP_200_OK)
    else:
        return Response({'message': -1}, status=status.HTTP_400_BAD_REQUEST)

@swagger_auto_schema(method='PATCH', operation_description="O'chirmoqchi bo'lgan Profileni ID sini kirting")
@api_view(['PATCH'])
def verify_email(request, pk):
    if request.method == 'PATCH':
        try:
            profile = Profile.objects.get(id=pk)
        except:
            return Response({'message': -2}, status=status.HTTP_400_BAD_REQUEST)
        is_data = int(time.time())
        profile.is_verified = is_data
        profile.save()
        return Response({'message': 1}, status=status.HTTP_200_OK)
    else:
        return Response({'message': -1}, status=status.HTTP_400_BAD_REQUEST)

@swagger_auto_schema(method='POST', request_body=ProfilesingupSerialazer, operation_description="Malumotlarni kirting")
@api_view(['POST'])
def signup(request):
    if request.method == "POST":
        profiles = Profile.objects.all()
        usernames = [profile.username for profile in profiles]
        username = request.data.get('username')
        email = request.data.get('email')
        gm = [profile.email for profile in profiles]
        serializer = ProfileSerializer(data=request.data)
        if username in usernames:
            return Response({'message': -2}, status=status.HTTP_400_BAD_REQUEST)
        elif email in gm:
            return Response({'message': -2}, status=status.HTTP_400_BAD_REQUEST)
        elif serializer.is_valid():
            serializer.save()
            return Response({'message': 1,"profile":serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({'message': -1}, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response({'message': -1}, status=status.HTTP_400_BAD_REQUEST)

@swagger_auto_schema(methods='GET')
@api_view(['GET'])
def get_profile(request):
    if request.method == 'GET':
        profile = Profile.objects.all()
        serializer = ProfileSerializer(profile, many=True)
        return Response({'message': 1,"profile":serializer.data}, status=status.HTTP_200_OK)
    else:
        return Response({'message': -1},status=status.HTTP_400_BAD_REQUEST)

@swagger_auto_schema(methods='GET')
@api_view(['GET'])
def get_profile_id(request, pk):
    if request.method == 'GET':
        profile = Profile.objects.get(id=pk)
        serializer = ProfileSerializer(profile)
        return Response({'message': 1,"profile":serializer.data}, status=status.HTTP_200_OK)
    else:
        return Response({'message': -1},status=status.HTTP_400_BAD_REQUEST)
    
@swagger_auto_schema(methods='GET')
@api_view(['GET'])
def get_profile_username(request, username):
    if request.method == 'GET':
        profile = Profile.objects.get(username=username)
        serializer = ProfileSerializer(profile)
        return Response({'message': 1,"profile":serializer.data}, status=status.HTTP_200_OK)
    else:
        return Response({'message': -1},status=status.HTTP_400_BAD_REQUEST)
    
@swagger_auto_schema(method='POST', request_body=ProfileLoginserialazer, operation_description="Malumotlarni kirting")
@api_view(['POST'])
def login(request):
    if request.method == 'POST':
        username = request.data.get('username')
        password = request.data.get('password')
        try:
            profile = Profile.objects.get(username=username)
        except:
            return Response({'message': -2}, status=status.HTTP_400_BAD_REQUEST)
        if profile:
            if profile.password == password:
                profile_serializer = ProfileSerializer(profile)
                return Response({'message': 1, "profile":profile_serializer.data}, status=status.HTTP_200_OK)
            else:
                return Response({'message': -2}, status=status.HTTP_400_BAD_REQUEST)
        return Response({'message': -2}, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response({'message': -1}, status=status.HTTP_400_BAD_REQUEST)

@swagger_auto_schema(method='PATCH', request_body=UpdateProfileserialazer, operation_description="Yangilamaoqchi bo'lgan Profilening ID sini kirting")
@api_view(['PATCH'])
def update_profile(request, pk):
    if request.method == "PATCH":
        profile = Profile.objects.get(id=pk)        
        data = ProfileSerializer(instance=profile, data=request.data)
        if data.is_valid():
            # Profilni o'zgartirishni boshlashdan oldin
            new_username = data.validated_data.get('username')
            new_email = data.validated_data.get('email')

            # Check if the new username and email are unique
            if Profile.objects.filter(username=new_username).exclude(id=pk).exists():
                return Response({'message': -4}, status=status.HTTP_400_BAD_REQUEST)

            if Profile.objects.filter(email=new_email).exclude(id=pk).exists():
                return Response({'message': -3}, status=status.HTTP_400_BAD_REQUEST)

            # Agar muvaffaqiyatli tekshiruvdan o'tsangiz, profildagi ma'lumotlarni yangilang
            data.save()
            return Response({'message': 1,"profile":data.data}, status=status.HTTP_200_OK)
        else:
            return Response({'message': -2}, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response({'message': -1}, status=status.HTTP_400_BAD_REQUEST)
    
@swagger_auto_schema(method='DELETE', operation_description="O'chirmoqchi bo'lgan Profileni ID sini kirting")
@api_view(['DELETE'])
def delete_profile(request, pk):
    if request.method == 'DELETE':
        try:
            praduct = Profile.objects.get(id=pk)
        except:
            return Response({'message': -2 },status=status.HTTP_400_BAD_REQUEST)
        praduct.delete()
        return Response({'message':1},status=status.HTTP_200_OK)
    else:
        return Response({'message': -1 },status=status.HTTP_400_BAD_REQUEST)
    
@swagger_auto_schema(method='PATCH', request_body=ProfileRefeleshSerialazer, operation_description="Referal_link")
@api_view(['PATCH'])
def activate_referral_link(request, pk):
    if request.method == 'PATCH':
        referal = request.data.get('referal_link')
        try:
            frend = Profile.objects.get(referal_link=referal)
        except:
            return Response({'message': -2}, status=status.HTTP_400_BAD_REQUEST)
        profile = Profile.objects.get(id=pk)
        profile.balance += 5
        profile.save()
        frend.balance += 5
        frend.save()
        return Response({'message': 1}, status=status.HTTP_200_OK)
    else:
        return Response({'message': -1},status=status.HTTP_400_BAD_REQUEST)
    
@swagger_auto_schema(method='PATCH', operation_description="Ball berladigan profile ID sini kirting")
@api_view(['PATCH'])
def ad_reward(request, pk):
    if request.method == 'PATCH':
        try:
            profile = Profile.objects.get(id=pk)
        except:
            return Response({'message': -2},status=status.HTTP_400_BAD_REQUEST)    
        profile.balance += 2
        profile.save()
        return Response({'message': 1},status=status.HTTP_200_OK)
    else:
        return Response({'message': -1},status=status.HTTP_400_BAD_REQUEST)