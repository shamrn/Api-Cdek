from django.urls import path
from . import views

urlpatterns = [
    path('',views.product,name='product'),
    path('order/<pk>/',views.product_order,name='order'),
    path('to_html',views.to_html,name='to_html')
]