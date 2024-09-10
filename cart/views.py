from django.shortcuts import render, get_object_or_404
from .cart import Cart
from product.models import Product
from django.http import JsonResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def cart_summary(request):
    cart = Cart(request)
    cart_products = cart.get_product()
    quantities = cart.get_quantity()
    totals = cart.cart_total()
    return render(request, "cart_summary.html", {'cart_products': cart_products, 'quantities': quantities, 'totals': totals})

@login_required
def cart_add(request):
    # Get the cart
    cart = Cart(request)
    # Test for POST
    if request.POST.get('action') == 'post':
        # Get the data
        product_id = int(request.POST.get('product_id'))
        product_qty = int(request.POST.get('product_qty'))
        # Lookup product in DB
        product = get_object_or_404(Product, id=product_id)
        # Save to session
        cart.add(product=product, quantity=product_qty)
        # Get cart quantity
        cart_quantity = cart.__len__()
        # Return response
        response = JsonResponse({'qty': cart_quantity})
        messages.success(request, "Item has been added to your Shopping Cart...")
        return response

@login_required
def cart_delete(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        # Get the data
        product_id = int(request.POST.get('product_id'))
        # Call delete function in Cart
        cart.delete(product_id)
        # Return response
        response = JsonResponse({'product': product_id})
        messages.error(request, "Item Deleted From Shopping Cart...")
        return response

@login_required
def cart_update(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        # Get the data
        product_id = int(request.POST.get('product_id'))
        product_qty = int(request.POST.get('product_qty'))
        # Update the cart
        cart.update(product_id, product_qty)
        # Return response
        response = JsonResponse({'qty': product_qty})
        messages.warning(request, "Your Cart Has Been Updated...")
        return response
