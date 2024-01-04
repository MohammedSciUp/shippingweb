from django.db import models

# Create your models here.


class Order(models.Model):
    STATUS_CHOICES = [
        ('confirmed', 'Confirmed (China Office)'),
        ('collected', 'Collected (China Office)'),
        ('shipped', 'Shipped'),
        ('arrived', 'Arrived (Oman Office)'),
        ('received', 'Received by customer'),
    ]

    customer_name = models.CharField(max_length=100)
    customer_phone_number = models.CharField(max_length=8)
    order_reference_number = models.CharField(max_length=100, unique=True)
    order_description = models.TextField()
    order_status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='confirmed')

    def __str__(self):
        return f"{self.order_reference_number} - {self.customer_name}"


class OrderStatusUpdate(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='status_updates')
    status = models.CharField(max_length=50, choices=Order.STATUS_CHOICES)
    update_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-update_date']

    def __str__(self):
        return f"{self.order.order_reference_number} - {self.status} on {self.update_date}"




class ShippingRate(models.Model):
    cbm = models.DecimalField(max_digits=5, decimal_places=2, unique=True)
    price = models.DecimalField(max_digits=10, decimal_places=3)

    def __str__(self):
        return f"{self.cbm} CBM - {self.price} OMR"

class ContainerLaunch(models.Model):
    launch_date = models.DateField()

    def __str__(self):
        return f"Next Launch: {self.launch_date}"






# Remember to make migrations after defining your model
# python manage.py makemigrations
# python manage.py migrate
#path('', views.track, name='track'),
