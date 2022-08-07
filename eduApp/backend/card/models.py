from django.db import models
from django.contrib.auth.models import User


class Card(models.Model):
    class Meta:
        db_table = "card"

    card_id = models.AutoField(primary_key=True)
    card_name = models.TextField(max_length=500, null=True, blank=True)
    card_image = models.ImageField(upload_to='card_images', blank=True, null=True)
    card_price = models.DecimalField(max_digits=10, decimal_places=0)
    card_description = models.TextField(max_length=500, null=True, blank=True)
    card_enable = models.BooleanField(null=True, blank=True, default=True)
    card_status = models.BooleanField(null=True, blank=True, default=True)
    card_user_created = models.ForeignKey(
        User, related_name='card_user_created',
        on_delete=models.SET_NULL, null=True, blank=True
    )
    card_user_updated = models.ForeignKey(
        User, related_name='card_user_updated',
        on_delete=models.SET_NULL, null=True, blank=True
    )
    card_created_at = models.DateTimeField(auto_now_add=True)
    card_updated_at = models.DateTimeField(auto_now=True)


# class Cart(models.Model):
#     class Meta:
#         db_table = "cart"
#
#     cart_id = models.AutoField(primary_key=True)
#     cart_code = models.CharField(max_length=50, null=True, blank=True)
#     cart_date = models.DateTimeField(auto_now_add=True)
#     cart_total = models.DecimalField(max_digits=10, decimal_places=0)
#     cart_full_name = models.TextField(max_length=50, null=True, blank=True)
#     cart_email = models.CharField(max_length=254, null=True, blank=True)
#     cart_phone_number = models.CharField(max_length=254, null=True, blank=True)
#     cart_user_created = models.ForeignKey(
#         User, related_name='cart_user_created',
#         on_delete=models.SET_NULL, null=True, blank=True
#     )
#     cart_user_updated = models.ForeignKey(
#         User, related_name='cart_user_updated',
#         on_delete=models.SET_NULL, null=True, blank=True
#     )
#     cart_created_at = models.DateTimeField(auto_now_add=True)
#     cart_updated_at = models.DateTimeField(auto_now=True)
#
#
# class CartItem(models.Model):
#     class Meta:
#         db_table = "cart_item"
#
#     cart_item_id = models.AutoField(primary_key=True)
#     cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
#     card = models.ForeignKey(Card, on_delete=models.CASCADE)
#     cart_item_quantity = models.IntegerField(default=1)
#     cart_item_price = models.DecimalField(max_digits=10, decimal_places=0)
#     cart_item_total = models.DecimalField(max_digits=10, decimal_places=0)
#     cart_item_date = models.DateTimeField(auto_now_add=True)
#     cart_item_user_created = models.ForeignKey(
#         User, related_name='cart_item_user_created',
#         on_delete=models.SET_NULL, null=True, blank=True
#     )
#     cart_item_user_updated = models.ForeignKey(
#         User, related_name='cart_item_user_updated',
#         on_delete=models.SET_NULL, null=True, blank=True
#     )
#     cart_item_created_at = models.DateTimeField(auto_now_add=True)
#     cart_item_updated_at = models.DateTimeField(auto_now=True)

