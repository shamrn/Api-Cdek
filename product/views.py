from django.shortcuts import render, redirect
from .models import Product
from .cdek_api import get_region, get_cities, get_cost_delivery

from django.core.mail import send_mail
from django.template import loader

def product(request):
    products = Product.objects.all()
    return render(request, 'product/product.html', {'products': products})


def product_order(request, pk):
    product = Product.objects.get(pk=pk)
    regions = get_region()  # вызываем функцию, которая выдает словарь регионов сдека
    cities = None
    data_delivery = None
    message_error = None
    if 'region' in request.GET:
        cities = get_cities(
            request.GET['region'])  # вызываем функцию, которая выдает словарь городов по выбранному региону
    if 'city' in request.GET:
        data_delivery = get_cost_delivery(city_code=request.GET['city'],
                                          weight=product.weight,
                                          length=product.length,
                                          width=product.width,
                                          height=product.height)
        if 'errors' in data_delivery:
            message_error = (dict(*data_delivery['errors'])['message'])

    return render(request, 'product/product_order.html', {'product': product,
                                                          'regions': regions,
                                                          'cities': cities,
                                                          'data_delivery':data_delivery,
                                                          'message_error':message_error})

def to_html():
    html_message = loader.render_to_string('product/to_html.html')
    send_mail('html файл', 'html файл', 'shamrin2007@mail.ru',['iamslamduck@gmail.com'],
              fail_silently=True, html_message=html_message)
    return redirect('product')