from django.urls import path
from . import views

urlpatterns = [
    path('', views.track, name='track'),
    path('neworder/', views.create_order, name='create_order'),
    path('ordersuccess/', views.order_success, name='order_success'),
    path('updateorderstatus/', views.update_order_status, name='update_order_status'),
    path('login/', views.login_view, name='login_view'),
    
    path('tracking/', views.track_order, name='track_order'),
    path('logout/', views.logout_view, name='logout'),
    
]