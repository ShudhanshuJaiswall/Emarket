from django.db import models


class Category(models.Model):    
    cateName = models.CharField(max_length=50,null=False,unique=True)

    def __str__(self):
        return self.cateName

class Product(models.Model):
    prodName = models.CharField(max_length=50,null=False)
    description = models.CharField(max_length=100)
    prodPrice = models.FloatField(null=False)
    category = models.ForeignKey(to=Category,on_delete=models.CASCADE)
    pic1 = models.CharField(max_length=100)
    pic2 = models.CharField(max_length=100)
    pic3 = models.CharField(max_length=100)

    def __str__(self):
        return self.prodName

