from django.urls import path
from .views import home

app_name = "stock"

urlpatterns = [
    path("products/", home, name="home"),
    path("products/<str:product_id>/", home, name="detail")
]