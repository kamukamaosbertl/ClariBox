from django.urls import path
from django.contrib.auth import views as auth_views # Import built-in login/logout views
from . import views

urlpatterns = [
    # --- Custom Dashboard Paths ---
    # This makes 'your-site.com/dashboard/' load your main custom interface
    path('', views.admin_dashboard, name='admin_dashboard'),
    
    path('ai/', views.ai_assistant, name='ai_assistant'),
    path('categories/', views.category_insights, name='category_insights'),
    path('reports/', views.reports, name='reports'),
    path('settings/', views.settings_view, name='settings'),
    path('alert/<int:alert_id>/', views.alert_detail, name='alert_detail'),

    # --- Secure Authentication Paths ---
    # Login page (Uses your custom registration/login.html)
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),

    # Logout functionality (Redirects back to login page)
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
]