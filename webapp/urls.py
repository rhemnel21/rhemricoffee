from django.urls import path
from . import views
from .views import create_order
from .views import order_list, order_detail, order_new, order_edit, order_delete




urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('about/', views.about_page, name='about_page'),
    path('contact/', views.contact_page, name='contact_page'),
    path('menu/', views.menu_page, name='menu_page'),
    path('order/', views.order_page, name='order_page'),
    path('placeorder/', views.placeorder_page, name='placeorder_page'),
    path('final/', views.final_page, name='final_page'),
    path('navbar/', views.nav_bar, name='nav_bar'),
    path('create_order/', create_order, name='create_order'),
    path('orders/', order_list, name='order_list'),
    path('orders/<int:pk>/', order_detail, name='order_detail'),
    path('orders/new/', order_new, name='order_new'),
    path('orders/<int:pk>/edit/', order_edit, name='order_edit'),
    path('orders/<int:pk>/delete/', order_delete, name='order_delete'),
]