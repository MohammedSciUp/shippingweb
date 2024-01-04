from django import forms
from django.db import models
from .models import Order

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['customer_name', 'customer_phone_number', 'order_reference_number', 'order_description', 'order_status']
        widgets = {
            'order_description': forms.Textarea(attrs={'rows': 4, 'cols': 40}),
            'order_status': forms.Select()
        }

class OrderSearchForm(forms.Form):
    search = forms.CharField(label='Order Reference or Phone Number', max_length=100)

    def search_order(self):
        search_value = self.cleaned_data['search']
        try:
            order = Order.objects.get(
                models.Q(order_reference_number=search_value) |
                models.Q(customer_phone_number=search_value)
            )
            return order
        except Order.DoesNotExist:
            return None

class OrderStatusUpdateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['order_status']
        widgets = {
            'order_status': forms.Select()
        }

class OrderTrackForm(forms.Form):
    tracking_number = forms.CharField(label='Tracking Number or Phone', max_length=50)