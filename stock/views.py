from django.shortcuts import render, redirect
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
        picture = request.FILES.get("picture", None)

        if product:
            product.name = name
            product.price = price
            product.unit = unit
            product.all_quantity = product.all_quantity - product.current_quantity + int(quantity)
            product.current_quantity = quantity
            product.save()
        else:
            product = Product(
                name=name,
                price=price,
                unit=unit,
                current_quantity=quantity,
                all_quantity=quantity
            )
        if picture is not None:
            product.picture = picture
            product.save()
    
    context = {
        "products": products,
        "transactions": all_movements,
        "product_movements": product_movements,
        "product": product
    }

    return render(request, "home.html",context=context)

def add_transaction(request, product_id):
    if request.method == "POST":
        category = request.POST.get("category")
        quantity = request.POST.get("quantity", 0)
        comment = request.POST.get("comment")

        product = Product.objects.filter(id=product_id).first()

        if product is not None:
            ProductMovement.objects.create(
                product=product,
                category=category,
                quantity=quantity,
                comment=comment
            )
            if category.upper() == "IN":
                product.current_quantity = product.current_quantity + int(quantity)
                product.all_quantity = product.all_quantity + int(quantity)
            elif category.upper() == "OUT":
                product.current_quantity = product.current_quantity - int(quantity)
            product.save()
    return redirect("stock:home")
    