from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.http import HttpResponse
from django.conf import settings
from django.contrib import messages

# Create your views here.
def index(request):
    if request.method == "POST":
        receiver_email = request.POST['receiver_email']
        subject = request.POST['subject']
        message = request.POST['message']
        from_email = settings.EMAIL_HOST_USER  # Change to your email

        try:
            send_mail(subject, message, from_email, [receiver_email])
            messages.success(request, "✅ Email sent successfully!")  # Success message
            return redirect('index')  # Redirect to prevent resubmission
        except Exception as e:
            messages.error(request, f"❌ Failed to send email: {e}")  # Error message
            return redirect('index')  # Redirect even on failure to avoid stuck page
    return render(request, 'index.html')