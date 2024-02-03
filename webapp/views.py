from django.shortcuts import HttpResponse, render


def home_page(request):
    return render(request, "pages/home.html")

def about_page(request):
    return render(request, "pages/about.html")

def contact_page(request):
    return render(request, "pages/contact.html")

def menu_page(request):
    return render(request, "pages/menu.html")

def order_page(request):
    return render(request, "pages/order.html")

def placeorder_page(request):
    return render(request, "pages/placeorder.html")

def final_page(request):
    return render(request, "pages/final.html")

def nav_bar(request):
    return render(request, "pages/navbar.html")



from django.shortcuts import render, redirect
from .forms import OrderForm


def create_order(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save()
            # Assuming 'order_page' is the name of the URL pattern for 'order.html'
            return redirect('home_page')  # Update with the correct URL name
    else:
        form = OrderForm()

    return render(request, 'pages/create_order.html', {'form': form})


# in views.py
from django.shortcuts import render, get_object_or_404, redirect
from .models import Order
from .forms import OrderForm

def order_list(request):
    orders = Order.objects.all()
    return render(request, 'pages/order_list.html', {'orders': orders})

def order_detail(request, pk):
    order = get_object_or_404(Order, pk=pk)
    return render(request, 'pages/order_detail.html', {'order': order})

def order_new(request):
    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save()
            return redirect('pages/order_detail', pk=order.pk)
    else:
        form = OrderForm()
    return render(request, 'pages/order_edit.html', {'form': form})

def order_edit(request, pk):
    order = get_object_or_404(Order, pk=pk)

    if request.method == "POST":
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            order = form.save()
            return redirect('order_detail', pk=order.pk)
    else:
        form = OrderForm(instance=order)

    return render(request, 'pages/order_edit.html', {'form': form, 'order': order})


def order_delete(request, pk):
    order = get_object_or_404(Order, pk=pk)
    order.delete()
    return redirect('order_list')
