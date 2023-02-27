from django.db import models

# Create your models here.
class category(models.Model):
    name=models.CharField(max_length=100)
    img=models.ImageField(upload_to="pic")
    date=models.DateTimeField(auto_now_add=True)
    