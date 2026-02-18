from django.urls import path
from django.contrib.auth.decorators import login_required # The Gatekeeper
from . import views

urlpatterns = [
    # Public pages
    path('', views.welcome, name='welcome'), 
    path('helpline/', views.helpline, name='helpline'),
    
    # Protected page - Login is forced here
    path('submit/', login_required(views.submit_feedback), name='submit_feedback'), 
    
    # Post-submission pages
    path('success/', views.success_page, name='success_page'),
]