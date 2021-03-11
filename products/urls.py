from django.urls import path

from products.views import ProductView

urlpatterns = [
    path('products/<int:pk>/', ProductView.as_view())
]
