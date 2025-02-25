from django.shortcuts import render
from django.core.mail import send_mail
from django.http import HttpResponse
from django.conf import settings

# Create your views here.
def index(request):
    if request.method == "POST":
        receiver_email = request.POST['receiver_email']
        subject = request.POST['subject']
        message = request.POST['message']
        from_email = settings.EMAIL_HOST_USER  # Change to your email

        try:
            send_mail(subject, message, from_email, [receiver_email])
            return HttpResponse("Email sent successfully!")
        except Exception as e:
            return HttpResponse(f"Error: {e}")
    return render(request, 'index.html')