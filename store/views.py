from django.shortcuts import render
from .models import *

# Create your views here.
def store(request):
    products = Product.objects.all() # Get all the products in the database
    context = {'products':products}  # Pass the data to the template
    return render(request, 'store/store.html', context)

def cart(request):
    
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete = False)
        items = order.orderitem_set.all()
    else:
        items = []
        order = {'get_cart_total':0, 'get_order_items':0}

    context = {'items':items, 'order':order}
    return render(request, 'store/cart.html', context)

def checkout(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
    else:
        # Create an empty cart for the non-logged user
        order = {'get_cart_total':0, 'get_cart_items':0}
        items = []
    context = {'items':items, 'order': order}
    return render(request, 'store/checkout.html', context)