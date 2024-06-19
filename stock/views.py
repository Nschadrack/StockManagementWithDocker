from django.shortcuts import render
from .models import Product, ProductMovement

# Create your views here.
def home(request, product_id=None):
    products = Product.objects.all().order_by("-recorded_date")
    all_movements = ProductMovement.objects.all().order_by("-movement_date")
    product = products.filter(id=product_id).first()
    product_movements = all_movements.filter(product=product)
    if request.method == "POST":
        name = request.POST.get("name")
        price = request.POST.get("price")
        unit = request.POST.get("unit")
        quantity = request.POST.get("quantity", 0)

        if product:
            product.name = name
            product.price = price
            product.unit = unit
            product.all_quantity = product.all_quantity - product.current_quantity + int(quantity)
            product.current_quantity = quantity
            product.save()
        else:
            Product.objects.create(
                name=name,
                price=price,
                unit=unit,
                current_quantity=quantity,
                all_quantity=quantity
            )
    
    context = {
        "products": products,
        "all_movements": all_movements,
        "product_movements": product_movements,
        "product": product
    }

    return render(request, "home.html",context=context)

    