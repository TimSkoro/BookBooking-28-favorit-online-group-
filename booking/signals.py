from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models import Employer


@receiver(pre_save, sender=Employer)
def my_handler(sender, instance, **kwargs):
    if not instance.id:
        instance.changed_count += 1
        instance.cart = Cart.objects.create(cart_name=f"Cart {instance.username}")
