# from django.core.mail import EmailMessage
# from django.db.models.signals import post_save
# from django.dispatch import receiver
# from django.template.loader import render_to_string
# from .models import Order

# @receiver(post_save, sender=Order)
# def send_order_alert(sender, instance, created, **kwargs):
#     if created:
#         order_items = instance.order_items.all()
#         subject = 'New Order Alert'
#         message = render_to_string('order_alert_email.html', {
#             'order': instance,
#             'order_items': order_items,
#         })
        
#         email = EmailMessage(
#             subject=subject,
#             body=message,
#             from_email='hamroagrofarm@gmail.com',
#             to=['hamroagrofarm@gmail.com'],
#             headers={'Content-Type': 'text/html'}
#         )
#         email.send()
