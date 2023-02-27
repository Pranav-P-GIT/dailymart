from django.db import models
from home.models import category

# Create your models here.
class product(models.Model):
    cate=models.ForeignKey(category,related_name="products",on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    price=models.IntegerField()
    quantity=models.IntegerField()
    img=models.ImageField(upload_to="pic")
    disc=models.TextField()
    discount=models.IntegerField(default=0)
    date=models.DateTimeField(auto_now_add=True)