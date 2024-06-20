from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=150, null=False, blank=False)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=False)
    unit = models.CharField(max_length=40, blank=False, null=False)
    current_quantity = models.PositiveIntegerField(default=0)
    all_quantity = models.PositiveIntegerField(default=0)
    recorded_date = models.DateTimeField(auto_now_add=True)
    picture = models.ImageField(upload_to="uploaded_images/", null=True, blank=True)

    class Meta:
        db_table = "products"
    
    def __str__(self) -> str:
        return f"Product: {self.name}"
    

class ProductMovement(models.Model):
    MOVEMENT_TYPE = (("IN", "IN"),
                     ("OUT", "OUT"))
    
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    category = models.CharField(choices=MOVEMENT_TYPE, default="IN", max_length=8)
    movement_date = models.DateTimeField(auto_now_add=True)
    quantity = models.PositiveIntegerField()
    comment = models.CharField(max_length=255)

    class Meta:
        db_table = "product_movements"

    def __str__(self) -> str:
        if self.category.upper() == "IN":
            return f"Product: {self.product.name} has increased by {self.quantity}"
        else:
            return f"Product: {self.product.name} has decreased by {self.quantity}"