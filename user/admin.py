# your_app_name/admin.py
from django.contrib import admin
from .models import Profile
from django.http import HttpResponse
from django.urls import path

class ProfileAdmin(admin.ModelAdmin):
    # Profile modelini admin panelga qo'shish uchun ma'lumotlar
    list_display = ('username', 'email', 'is_verified', 'is_archived')  # O'zgaruvchilarni o'zgartiring
    search_fields = ('username', 'email')  # O'zgaruvchilarni o'zgartiring

    def get_number_of_profiles(self, request):
        profiles_count = Profile.objects.count()
        return HttpResponse(f"Number of profiles: {profiles_count}")

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('get_number_of_profiles/', self.admin_site.admin_view(self.get_number_of_profiles), name='get_number_of_profiles'),
        ]
        return custom_urls + urls

# ProfileAdmin ni boshqa xususiyatlar bilan birgalikda qo'shing
admin.site.register(Profile, ProfileAdmin)
