from django.urls import path
from . import views


urlpatterns = [

    path('signup/', views.signup, name='signup'),
    path('get-profiles/', views.get_profil, name='get-profiles'),
    path('login/', views.login_view, name='login'),
    path('get-profile-id/<str:pk>/', views.get_profil_pk, name='get-profile-id'),
    path('update-profile/<str:pk>/', views.profile_update, name='update-profile'),
    path('delete-profile/<str:pk>/', views.profile_delete, name='delete-profile'),
    path('referal-link/<str:pk>/', views.referal_link, name='referal-link'),
    path('ball/<str:pk>/', views.ball, name='ball'),
    # path('confirmation/<str:username>/', views.confirmation, name='confirmation'),
    path('delete-later/<str:pk>/', views.delete_later, name='delete-later')
   
]