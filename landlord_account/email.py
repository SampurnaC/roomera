from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string
from .tokens import generate_verification_token
from django.urls import reverse

def send_verification_email(user, request):
    token, uid = generate_verification_token(user)
    
    verification_url = request.build_absolute_uri(
        reverse("landlord_account:verify_email", kwargs={"uidb64": uid, "token": token})
    )
    
    subject = "Verify Your Email"
    message = render_to_string("landlord_account/verify_email.html", {
        "user": user,
        "verification_link": verification_url
    })

    send_mail(
        subject,
        message,
        settings.DEFAULT_FROM_EMAIL,
        [user.email],
        fail_silently=False,
        html_message=message
    )
