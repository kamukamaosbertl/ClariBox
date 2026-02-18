from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # Fixed line: changed .admin to .urls
    path('admin/', admin.site.urls), 

    # This line connects the Google SSO routes
    path('accounts/', include('allauth.urls')),
    
    path('', include('SuggestionBox.urls')), 
    path('dashboard/', include('dashboard.urls')),
]