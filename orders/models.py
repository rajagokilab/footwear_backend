# # orders/models.py
# from django.db import models
# from products.models import Product
# import uuid
# from django.contrib.auth.models import User


# class Order(models.Model):
#     ORDER_STATUS = [
#         ('PLACED', 'Order Placed'),
#         ('DISPATCHED', 'Order Dispatched'),
#         ('IN_TRANSIT', 'In Transit'),
#         ('DELIVERED', 'Delivered'),
        
#     ]

#     order_id = models.CharField(max_length=20, unique=True, editable=False)
#     product = models.ForeignKey(Product, on_delete=models.CASCADE)
#     user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
#     quantity = models.IntegerField()
#     total_price = models.DecimalField(max_digits=10, decimal_places=2)
#     status = models.CharField(max_length=20, choices=ORDER_STATUS, default='PLACED')
#     created_at = models.DateTimeField(auto_now_add=True)
    
#     def save(self, *args, **kwargs):
#         if not self.order_id:
#             self.order_id = f"BH{uuid.uuid4().hex[:8].upper()}"
#         super().save(*args, **kwargs)
# orders/models.py
from django.db import models
from products.models import Product
import uuid
from django.contrib.auth.models import User

class Order(models.Model):
    ORDER_STATUS = [
        ('PLACED', 'Order Placed'),
        ('DISPATCHED', 'Order Dispatched'),
        ('IN_TRANSIT', 'In Transit'),
        ('DELIVERED', 'Delivered'),
    ]

    order_id = models.CharField(max_length=20, unique=True, editable=False)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    quantity = models.PositiveIntegerField(default=1)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, editable=False)
    status = models.CharField(max_length=20, choices=ORDER_STATUS, default='PLACED')
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        # Generate order_id automatically
        if not self.order_id:
            self.order_id = f"BH{uuid.uuid4().hex[:8].upper()}"
        # Auto-calculate total_price from product price * quantity
        if self.product and self.quantity:
            self.total_price = self.product.price * self.quantity
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.order_id} - {self.product.name} x{self.quantity} (${self.total_price})"
