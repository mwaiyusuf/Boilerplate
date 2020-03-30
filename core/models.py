from django.conf import settings
from django.db import models

# Create your models here.

# it will be avin the items(products)
class Item(models.Model):
    title = models.CharField(max_lenght=100)
    price = models.FloatField()

    def __str__(self):
        return self.title

    


class OrderItem(models.MOdel):
    item = models.ForeignKey(Item, on_delete = models.CASCADE)


    def __str__(self):
        return self.title
    

# we will be havin the cart items here 
class  Order(models.Model):
    user = foreignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)
    items = models.ManyToManyField(OrderItem)
    start_date = models.DateTimeField(auto_now_add=True)
    ordered_date = models.DateTimeField()
    ordered = models.BooleanField(default=False)


    def __str__(self):
        return self.user.username

    
