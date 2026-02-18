from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_protect
from .models import Suggestion

# 1. Shows the "Welcome" landing page (Public)
def welcome(request):
    # AUTO-CLEAN: Removes any student users who logged in but didn't submit.
    User.objects.filter(is_superuser=False, is_staff=False).delete()
    return render(request, 'SuggestionBox/welcome.html')

# 2. Handles the suggestion form (Protected by Google SSO)
@login_required
@csrf_protect # Ensures the security token is checked BEFORE shredding
def submit_feedback(request):
    # GATEKEEPER: Ensure it's a MUST student
    if not request.user.email.endswith('std.must.ac.ug'):
        user_to_delete = request.user
        logout(request)
        if not user_to_delete.is_superuser:
            user_to_delete.delete()
        
        return render(request, 'SuggestionBox/welcome.html', {
            'error': 'Access denied. Please use your official university email (@std.must.ac.ug).'
        })

    if request.method == 'POST':
        # 1. Capture the data FIRST
        category = request.POST.get('category')
        content = request.POST.get('content')
        
        # 2. Save it to the database
        Suggestion.objects.create(category=category, content=content)
        
        # 3. Capture the user to delete
        user_to_shred = request.user
        
        # 4. LOGOUT (Ends the session safely)
        logout(request)
        
        # 5. DELETE (Removes the evidence)
        if not user_to_shred.is_superuser:
            user_to_shred.delete()
            
        return redirect('success_page')
    
    return render(request, 'SuggestionBox/suggestion_form.html')

# 3. Success page (The missing piece that was causing your error)
def success_page(request):
    return render(request, 'SuggestionBox/success.html')

# 4. Helpline page
def helpline(request):
    return render(request, 'SuggestionBox/helpline.html')