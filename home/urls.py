from django.urls import path
from home import views

urlpatterns = [
    path('', views.index,name='homepage'),
    path('list/', views.productlist,name='productlist'),
    path('product/', views.productpage,name='productpage'),
    path('billing/', views.billing,name='billingpage'),
    
    
]