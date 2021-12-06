from django.db import models
from master.models import Product

class User(models.Model):
    userName  = models.CharField(max_length=100,null=False)
    userEmail  = models.CharField(max_length=100,null=False)
    userPhone  = models.CharField(max_length=100,null=True)
    userPass  = models.CharField(max_length=10,null=False)
    userPic  = models.CharField(max_length=200,null=True)
    userAddress = models.CharField(max_length=500,null=True)
    otp = models.IntegerField()
    isverify = models.BooleanField(default=False)

class UserOrder(models.Model):
    orderDate = models.DateField(null=False)
    orderAmount = models.FloatField(null=False)
    user = models.ForeignKey(to=User,on_delete=models.CASCADE)
    status = models.IntegerField(default=1) # 1:orderplaced 2:accept 3:deliver

class OrderItems(models.Model):
    order = models.ForeignKey(to=UserOrder,on_delete=models.CASCADE)
    product = models.ForeignKey(to=Product,on_delete=models.CASCADE)
    amount = models.FloatField(null=False)