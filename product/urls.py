from urllib.parse import urlparse
from django.urls import path
from .views import AllProducts, SingleProduct


urlpatterns = [
    path('', AllProducts.as_view()),
    path('<int:pk>', SingleProduct.as_view()),
    path('update/<int:pk>', SingleProduct.as_view()),
    path('delete/<int:pk>', SingleProduct.as_view())
]