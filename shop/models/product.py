from django.db import models

class Product(models.Model):
    name=models.CharField(max_length=50)
    description=models.CharField(max_length=500)
    price=models.IntegerField(default=0)
    active=models.BooleanField(default=True)
    discount=models.IntegerField(default=0)    
    thumbnail=models.ImageField(upload_to='uploads/thumbnails')    

    def __str__(self):
        return self.name    


class ProductImage(models.Model):
    product=models.ForeignKey(Product,default=None, on_delete=models.CASCADE)
    image=models.ImageField(upload_to='uploads/images', blank=True)