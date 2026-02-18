from django.shortcuts import render, redirect
from django.utils import timezone
from datetime import timedelta
from django.db.models import Count
from SuggestionBox.models import Suggestion
from django.contrib.auth.decorators import login_required, user_passes_test

# --- Admin access check ---
def is_admin(user):
    # Only active staff/superusers can access the dashboard
    return user.is_active and (user.is_staff or user.is_superuser)

# --- DASHBOARD VIEW ---
@login_required(login_url='/admin/login/') 
@user_passes_test(is_admin, login_url='/admin/login/')
def admin_dashboard(request):
    total_feedback = Suggestion.objects.count()
    
    # Time Filters
    last_7_days = timezone.now() - timedelta(days=7)
    recent_feedback = Suggestion.objects.filter(created_at__gte=last_7_days)
    
    # Category Stats
    category_stats = (
        Suggestion.objects
        .values('category')
        .annotate(count=Count('id'))
        .order_by('-count')
    )

    context = {
        'admin_name': request.user.username,
        'total_feedback': total_feedback,
        'category_stats': category_stats,
    }
    return render(request, 'dashboard/index.html', context)

# --- AI ASSISTANT ---
@login_required(login_url='/admin/login/')
@user_passes_test(is_admin, login_url='/admin/login/')
def ai_assistant(request):
    return render(request, 'dashboard/ai.html')

# --- REPORTS ---
@login_required(login_url='/admin/login/')
@user_passes_test(is_admin, login_url='/admin/login/')
def reports(request):
    return render(request, 'dashboard/reports.html')

# --- CATEGORY INSIGHTS ---
@login_required(login_url='/admin/login/')
@user_passes_test(is_admin, login_url='/admin/login/')
def category_insights(request):
    return render(request, 'dashboard/categories.html')

# --- ALERT DETAIL ---
@login_required(login_url='/admin/login/')
@user_passes_test(is_admin, login_url='/admin/login/')
def alert_detail(request, alert_id):
    context = {"alert_id": alert_id}
    return render(request, "dashboard/alert_detail.html", context)

# --- SETTINGS ---
@login_required(login_url='/admin/login/')
@user_passes_test(is_admin, login_url='/admin/login/')
def settings_view(request):
    return render(request, 'dashboard/settings.html')