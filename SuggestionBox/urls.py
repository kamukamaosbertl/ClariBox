from django.urls import path
from . import views

urlpatterns = [
    # This makes 'http://127.0.0.1:8000/' show your Welcome page
    path('', views.welcome, name='welcome'), 
    
    # This makes 'http://127.0.0.1:8000/submit/' show the feedback form
    path('submit/', views.submit_feedback, name='submit_feedback'), 
    
    # These match the other pages in your ClariBox flow
    path('success/', views.success_page, name='success_page'),
    path('helpline/', views.helpline, name='helpline'),
]