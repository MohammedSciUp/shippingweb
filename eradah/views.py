
from django.shortcuts import render, redirect
from .forms import OrderForm, OrderSearchForm, OrderStatusUpdateForm, OrderTrackForm
from django.http import HttpResponse
from .models import Order, OrderStatusUpdate
from django.contrib.auth import authenticate, login,  logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .models import ShippingRate, ContainerLaunch
from django.db.models import Q


# Create your views here.

# - ----------------------------------------------------------------------------------------




def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('track')  # Redirect to a page for entering customer details
    else:
        form = AuthenticationForm()
    return render(request, 'eradah/loginpage.html', {'form': form})




# ------------------------------------------------------------------------------------------


def track(request):
    
    shipping_rates = ShippingRate.objects.all()
    container_launch = ContainerLaunch.objects.latest('launch_date')
    context = {
        'shipping_rates': shipping_rates,
        'container_launch': container_launch,
    }
    return render(request, 'eradah/index.html', context)

#------------------------------------------------------------------------------------------


def track_order(request):
    form = OrderTrackForm()
    orders = Order.objects.none()  # Empty queryset
    context = {'form': form, 'orders': orders}

    if 'tracking_number' in request.GET:
        form = OrderTrackForm(request.GET)
        if form.is_valid():
            tracking_number = form.cleaned_data['tracking_number']
            orders = Order.objects.filter(
                Q(order_reference_number=tracking_number) |
                Q(customer_phone_number=tracking_number)
            )
            context['orders'] = orders

    return render(request, 'eradah/tracking.html', context)


#------------------------------------------------------------------------------------------
# def logging(request):
#     return render(request, 'eradah/base.html')
def logout_view(request):
    logout(request)
    return redirect('track')
#-------------------------------------------------------------------------------------------
@login_required
def create_order(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()  # This saves the new order along with its initial status
            return redirect('order_success')
    else:
        form = OrderForm()
    return render(request, 'eradah/neworder.html', {'form': form})
# ------------------------------------------------------------------------------------------
def order_success(request):
    # The order_success view no longer needs an order_id since it's not updating status.
    return render(request, 'eradah/success.html')

# ------------------------------------------------------------------------------------------
@login_required
def update_order_status(request):
    search_form = OrderSearchForm(request.GET or None)
    status_form = OrderStatusUpdateForm()
    order = None

    if search_form.is_valid():
        order = search_form.search_order()
        if order:
            # Populate the status form with the current status of the order
            status_form = OrderStatusUpdateForm(instance=order)

    if 'update_status' in request.POST:
        status_form = OrderStatusUpdateForm(request.POST)
        if status_form.is_valid():
            status = status_form.cleaned_data['order_status']
            OrderStatusUpdate.objects.create(order=order, status=status)
            # Update the order's status
            order.order_status = status
            order.save()

    return render(request, 'eradah/orderupdate.html', {
        'search_form': search_form,
        'status_form': status_form,
        'order': order
    })

# ------------------------------------------------------------------------------------------
