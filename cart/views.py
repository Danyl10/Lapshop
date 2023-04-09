from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from products.models import Laptop
from .cart import Cart
from .forms import CartAddLaptopForm


@require_POST
def cart_add(request, laptop_id):
    cart = Cart(request)
    laptop = get_object_or_404(Laptop, id=laptop_id)
    form = CartAddLaptopForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(laptop=laptop,
                 id = laptop_id,
                 quantity=cd['quantity'],
                 update_quantity=cd['update'])
    return redirect('cart:cart_detail')

def cart_remove(request, laptop_id):
    cart = Cart(request)
    laptop = get_object_or_404(Laptop, id=laptop_id)
    cart.remove(laptop)
    return redirect('cart:cart_detail')

def cart_detail(request):
    cart = Cart(request)
    return render(request, 'cart/detail.html', {'cart': cart})
# Create your views here.
