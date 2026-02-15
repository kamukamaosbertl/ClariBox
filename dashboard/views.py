from django.shortcuts import render, redirect
from django.utils import timezone
from datetime import timedelta
from django.db.models import Count
from SuggestionBox.models import Suggestion
from django.contrib.auth.decorators import login_required, user_passes_test

# --- Admin access check ---
def is_admin(user):
    # Only active staff users can access the dashboard
    return user.is_active and user.is_staff

# --- DASHBOARD VIEW ---
@login_required               # Require login
@user_passes_test(is_admin)  # Only allow staff
def admin_dashboard(request):
    """
    Main admin dashboard view.
    Shows total feedback, top category, and recent alerts (last 7 days).
    """

    # Total feedback overall
    total_feedback = Suggestion.objects.count()

    # --- TIME FILTERS ---
    last_7_days = timezone.now() - timedelta(days=7)
    recent_feedback = Suggestion.objects.filter(created_at__gte=last_7_days)
    recent_total = recent_feedback.count()  # Used for recent alert percentages

    # --- CATEGORY STATS (ALL-TIME) ---
    category_stats = (
        Suggestion.objects
        .values('category')
        .annotate(count=Count('id'))
        .order_by('-count')
    )

    # --- TOP CATEGORY (ALL-TIME) ---
    top_category_name = "None"
    top_category_percent = 0

    if total_feedback > 0 and category_stats.exists():
        top_category = category_stats.first()
        top_category_name = top_category['category'] or "Uncategorized"
        top_count = top_category['count']
        top_category_percent = round((top_count / total_feedback) * 100)

    # --- RECENT ALERTS LOGIC (LAST 7 DAYS) ---
    recent_alerts = []

    recent_category_stats = (
        recent_feedback
        .values('category')
        .annotate(count=Count('id'))
        .order_by('-count')
    )

    for stat in recent_category_stats:
        percent = round((stat['count'] / recent_total) * 100) if recent_total > 0 else 0

        if percent >= 30:
            recent_alerts.append({
                "id": stat['category'] or "uncategorized",
                "title": f"High volume of '{stat['category'] or 'Uncategorized'}' suggestions (Last 7 Days)",
                "new_reports": stat['count'],
                "count": stat['count'],
                "total": recent_total,
            })

    # --- CONTEXT FOR TEMPLATE ---
    context = {
        'admin_name': request.user.username,
        'total_feedback': total_feedback,
        'top_category_percent': top_category_percent,
        'top_category_name': top_category_name,
        'recent_alerts': recent_alerts,
    }

    return render(request, 'dashboard/index.html', context)


# --- AI ASSISTANT PAGE ---
@login_required
@user_passes_test(is_admin)
def ai_assistant(request):
    return render(request, 'dashboard/ai.html')


# --- ALERT DETAIL PAGE ---
@login_required
@user_passes_test(is_admin)
def alert_detail(request, alert_id):
    context = {
        "alert_id": alert_id
    }
    return render(request, "dashboard/alert_detail.html", context)


# --- CATEGORY INSIGHTS PAGE ---
@login_required
@user_passes_test(is_admin)
def category_insights(request):
    return render(request, 'dashboard/categories.html')


# --- REPORTS PAGE ---
@login_required
@user_passes_test(is_admin)
def reports(request):
    return render(request, 'dashboard/reports.html')


# --- SETTINGS PAGE ---
@login_required
@user_passes_test(is_admin)
def settings_view(request):
    return render(request, 'dashboard/settings.html')