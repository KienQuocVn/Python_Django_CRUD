from django.contrib import messages
from .models import Product
from django.shortcuts import render, redirect


def product_create(request):
  if request.method =="POST":
    name           = request.POST['name']
    price_purchase = float(request.POST['purchase_price'])
    price_selling  = float(request.POST['selling_price'])
    quantity        = int(request.POST['quantity'])

    item_product = Product(name=name, price_purchase=price_purchase, price_selling=price_selling, quantity=quantity)
    item_product.save()

    messages.success(request,"Sản pham da duoc tao thanh cong")

    return redirect('/')
  return render(request,'create.html',{})


def product_list(request):
  item_product = Product.objects.all()

  # Tính tổng doanh thu và lợi nhuận
  total_revenue = sum(
      item.price_selling * item.quantity_sold for item in item_product)
  total_profit = sum(
      (item.price_selling - item.price_purchase) * item.quantity_sold for item
      in item_product)

  return render(request, 'list.html', {
    "item_product": item_product,
    "total_revenue": total_revenue,
    "total_profit": total_profit
  })


def product_update(request, product_id):
  item_product = Product.objects.get(id = product_id)
  if request.method =="POST":
    item_product.name           = request.POST['name']
    item_product.price_purchase = float(request.POST['purchase_price'])
    item_product.price_selling  = float(request.POST['selling_price'])
    item_product.quantity       = int(request.POST['quantity'])
    item_product.quantity_sold  = int(request.POST['sold_quantity'])

    item_product.save()

    messages.success(request,"Sản pham da duoc cap nhat thanh cong")

    return redirect('/')
  return render(request,'update.html',{"item_product":item_product})

def product_delete(request, product_id):
  item_product = Product.objects.get(id = product_id)
  item_product.delete()
  messages.success(request, "Sản pham da duoc xoa thanh cong")

  return redirect('/')

def product_sell(request, product_id):
  item_product = Product.objects.get(id = product_id)
  quantity = int(request.GET.get('quantity'))
  item_product.quantity -= quantity
  item_product.quantity_sold +=quantity
  item_product.save()
  messages.success(request, "Sản pham da ban thanh cong")

  return redirect('/')