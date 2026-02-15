from django.shortcuts import render, redirect
from .models import Suggestion

# 1. Shows the "Welcome" landing page
def welcome(request):
    return render(request, 'SuggestionBox/welcome.html')

# 2. Handles the suggestion form
def submit_feedback(request):
    if request.method == 'POST':
        # If the student clicked 'Submit', grab the data from the form
        category = request.POST.get('category')
        content = request.POST.get('content')
        
        # Save it to the database (Notice we don't ask for names or IDs)
        Suggestion.objects.create(category=category, content=content)
        
        # Send them to the success page
        return redirect('success_page')
    
    # If they are just visiting the page, show them the blank form
    return render(request, 'SuggestionBox/suggestion_form.html')

# 3. Shows the "Feedback Submitted Successfully" page
def success_page(request):
    return render(request, 'SuggestionBox/success.html')

# 4. Shows the Helpline page for urgent reports (+256 306099876)
def helpline(request):
    return render(request, 'SuggestionBox/helpline.html')