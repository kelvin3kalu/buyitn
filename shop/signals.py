
# from django.contrib.auth.models import User
# from django.db.models.signals import post_save
# from django.contrib.auth.signals import user_logged_in
# from django.dispatch import receiver
# from django.core.mail import send_mail
# from django.conf import settings


# # Welcome email on account creation
# @receiver(post_save, sender=User)
# def send_welcome_email(sender, instance, created, **kwargs):
#     if created:
#         subject = 'Welcome to BuyIt'
#         message = f"Welcome {instance.username}, thank you for joining BuyIt!"
#         recipient_list = [instance.email]

#         send_mail(
#             subject,
#             message,
#             settings.EMAIL_HOST_USER,
#             recipient_list,
#             fail_silently=True,
#         )


# # Login notification email
# @receiver(user_logged_in)
# def send_login_email(sender, request, user, **kwargs):
#     subject = 'Login Notification'
#     message = f"Hello {user.username}, you just logged into your BuyIt account."

#     send_mail(
#         subject,
#         message,
#         settings.EMAIL_HOST_USER,
#         [user.email],
#         fail_silently=True,
#     )



from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.contrib.auth.signals import user_logged_in
from django.dispatch import receiver
import resend
from django.conf import settings


@receiver(post_save, sender=User)
def send_welcome_email(sender, instance, created, **kwargs):
    if created and instance.email:
        resend.api_key = settings.RESEND_API_KEY

        resend.Emails.send({
            "from": settings.DEFAULT_FROM_EMAIL,
            "to": [instance.email],
            "subject": "Welcome to BuyIt",
            "html": f"<p>Welcome {instance.username}, thank you for joining BuyIt!</p>",
        })


@receiver(user_logged_in)
def send_login_email(sender, request, user, **kwargs):
    if user.email:
        resend.api_key = settings.RESEND_API_KEY

        resend.Emails.send({
            "from": settings.DEFAULT_FROM_EMAIL,
            "to": [user.email],
            "subject": "Login Notification",
            "html": f"<p>Hello {user.username}, you just logged into your BuyIt account.</p>",
        })
