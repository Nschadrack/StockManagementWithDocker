from django.urls import path
from .views import home, add_transaction

app_name = "stock"

urlpatterns = [
    path("products/", home, name="home"),
    path("products/<str:product_id>/", home, name="detail"),
     path("products/<str:product_id>/add-transaction/", add_transaction, name="transaction")
]