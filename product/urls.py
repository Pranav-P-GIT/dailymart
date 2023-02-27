from django.urls import path
from product import views

urlpatterns = [
    path('', views.productlist,name='productlist'),
    path('product/', views.productpage,name='productpage'),
    path('product/billing/', views.billing,name='billingpage'),
    path('product/billing/thankyou', views.thankyou,name='thankyoupage'),
    
]
