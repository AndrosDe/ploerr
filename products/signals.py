'''imports'''
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from .models import UserReview, Container


@receiver(post_save, sender=UserReview)
def update_on_save(sender, instance, created, **kwargs):
    """
    Update product rating on product review update/create
    """
    if instance.product:
        instance.product.update()


@receiver(post_delete, sender=UserReview)
def update_on_delete(sender, instance, **kwargs):
    """
    Update product total on product review delete
    """
    if instance.product:
        instance.product.update()
