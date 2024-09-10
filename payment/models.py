from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User
from product.models import Product


# Create Order Model
class Order(models.Model):
    # Foreign Key
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    full_name = models.CharField(max_length=250)
    email = models.EmailField(max_length=250)
    shipping_address = models.TextField(max_length=15000)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    date_ordered = models.DateTimeField(auto_now_add=True)    
    shipping_status = models.BooleanField(default=False)
    date_shipped = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f'Order  by  {str(self.full_name)}  on  {self.date_ordered.strftime("%Y-%m-%d")}  of  Rs.{self.total_amount}  from  {self.shipping_address}'
    
    def save(self, *args, **kwargs):
        # Check if the shipping_status is being marked as True
        if self.shipping_status and not self.date_shipped:
            self.date_shipped = timezone.now()  # Correct usage of timezone.now()
        elif not self.shipping_status:
            self.date_shipped = None  # Reset the date if shipping status is False

        super().save(*args, **kwargs)


# Create Order Item Model
class OrderItem(models.Model):
    # Foreign Keys
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='order_items', null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    quantity = models.PositiveIntegerField(default=1)
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    subtotal = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return f'{str(self.product)} of Order Id: {self.order.id}'

    def save(self, *args, **kwargs):
        # Calculate subtotal
        self.subtotal = self.unit_price * self.quantity
        super().save(*args, **kwargs)
