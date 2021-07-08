from django.urls import path, include
from .views import *

urlpatterns = [
    path('v1/auth/login/',TokenLogin.as_view(),name="tokenLogin"),
    path('v1/products/',ProductDataAll,name="product")
]
