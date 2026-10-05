# WEEK5: Create a shopping cart web application and add a customized admin
# page for product catalog management for Experiment 3

# views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
#from django.contrib.auth import logout
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from .forms import RegistrationForm, CartItemForm
from .models import Product, CartItem


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('catalog')
    else:
        form = RegistrationForm()
    return render(request, 'registration.html', {'form': form})


@login_required
def catalog(request):
    products = Product.objects.all()
    return render(request, 'catalog.html', {'products': products})


@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart_item, created = CartItem.objects.get_or_create(user=request.user, product=product)
    if not created:
        cart_item.quantity += 1
    cart_item.save()
    return redirect('cart')


@login_required
def cart(request):
    items = CartItem.objects.filter(user=request.user)
    total = sum(item.subtotal() for item in items)
    return render(request, 'cart.html', {'items': items, 'total': total})


@login_required
def update_cart(request, item_id):
    item = get_object_or_404(CartItem, id=item_id, user=request.user)
    if request.method == 'POST':
        form = CartItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
    return redirect('cart')


#def user_logout(request):
#    logout(request)  # clears the session
#    return redirect('catalog')  # redirect to catalog or homepage
