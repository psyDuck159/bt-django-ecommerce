from django import views
from django.forms import ValidationError
from django.shortcuts import redirect, render
from .models import Bill, Book, BuyedItem, Cloth, Item, Laptop, MobilePhone, Shoe
from django.views import generic
from django.views.decorators.csrf import csrf_protect
from django.forms.models import model_to_dict
from django.db.transaction import get_autocommit, set_autocommit, commit, rollback

# Create your views here.
def index(request):
    books = Book.objects.all()[:4]
    clothes = Cloth.objects.all()[:4]
    laptops = Laptop.objects.all()[:4]
    mobiles = MobilePhone.objects.all()[:4]
    shoes = Shoe.objects.all()[:4]

    context = {
        'books': books,
        'clothes': clothes,
        'laptops': laptops,
        'mobiles': mobiles,
        'shoes': shoes,
    }

    return render(request, 'index.html', context=context)
# list view
class BookListView(generic.ListView):
    model = Book
class LaptopListView(generic.ListView):
    model = Laptop
class MobileListView(generic.ListView):
    model = MobilePhone
class ClothListView(generic.ListView):
    model = Cloth
class ShoeListView(generic.ListView):
    model = Shoe
# detail view
class BookDetailView(generic.DetailView):
    model = Book
class LaptopDetailView(generic.DetailView):
    model = Laptop
class MobileDetailView(generic.DetailView):
    model = MobilePhone
class ClothDetailView(generic.DetailView):
    model = Cloth
class ShoeDetailView(generic.DetailView):
    model = Shoe

def get_cart(request):
    cart = request.session.get('cart', {})
    cart_item = get_cart_items(cart)
    return render(request, 'cart.html', context={'cart': cart_item})

@csrf_protect
def add_to_cart(request):
    cart = request.session.get('cart', {})
    if request.method == 'POST':
        pk = request.POST['pk']
        if str(pk) in cart.keys():
            cart[pk] = cart[pk] + 1 if cart[pk] + 1 <= 10 else cart[pk]
        else:
            cart[pk] = 1
        request.session['cart'] = cart
        request.session.modified = True
        
        cart_item = get_cart_items(cart)
        return render(request, 'cart.html', context={'cart': cart_item})
    else:
        return redirect('cart')

@csrf_protect
def edit_cart(request):
    cart = request.session.get('cart', {})

    item_delete = []
    for key in cart:
        new_quantity = int(request.POST[key])
        if new_quantity != 0:
            cart[key] = new_quantity
        else:
            item_delete.append(key)
    for i in item_delete:
        cart.pop(i)
    request.session['cart'] = cart
    request.session.modified = True
    cart_item = get_cart_items(cart)
    return render(request, 'cart.html', context={'cart': cart_item})

@csrf_protect
def delete_cart(request):
    request.session['cart'] = {}
    request.session.modified = True
    return redirect('cart')

@csrf_protect
def buy(request):
    if request.method == 'POST':
        set_autocommit(False)
        cart = request.session.get('cart', {})
        name = request.POST['name']
        address = request.POST['address']
        tel = request.POST['tel']
        
        try:
            bill = Bill(customer=name, address=address, tel=tel)
            bill.save()
            for pk, quantity in cart.items():
                item = Item.objects.get(pk=pk)
                buyeditem = BuyedItem(item=item, bill=bill, price=item.price, quantity=quantity)
                buyeditem.save()
            commit() 
            request.session['cart'] = {}
            set_autocommit(True)
            return render(request, 'buy_result.html', context={'bill': bill})          
        except Exception:
            rollback()
            set_autocommit(True)
            return render(request, 'buy_result.html', context={'bill': bill, 'error': 'Có lỗi xảy ra'})           
    else:
        pass
        cart = request.session.get('cart', {})
        cart_item = {}
        total = 0.0
        for id, quantity in cart.items():
            item = Item.objects.get(pk=id)
            cart_item[item] = quantity
            total += item.price * quantity
        return render(request, 'buy_confirm.html', context={'cart': cart_item, 'total': total})

def get_cart_items(cart):
    cart_item = {}    
    for id, quantity in cart.items():
        item = Item.objects.get(pk=id)
        cart_item[item] = quantity
    return cart_item
