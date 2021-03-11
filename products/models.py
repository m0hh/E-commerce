from django.db import models
from django.contrib.auth.models import User

# Create your models here.
payment_methods = ((1,'credit card'),(2, 'cash'),(3, 'paypal'))

order_state = ((1,'Being Packaged'), (2, "On the way"), (3, 'Delivered'))

class Product(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to = 'images/') #, height_field=300, width_field=300)
    price = models.IntegerField()
    quantity = models.IntegerField()
    seller = models.ForeignKey(User, on_delete=models.CASCADE, related_name='products')
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Order(models.Model):
    item = models.ForeignKey(Product, on_delete= models.CASCADE, related_name='orders')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders')
    quantity = models.IntegerField()
    payment_options = models.CharField(choices=payment_methods, max_length=50)
    Delivery = models.CharField(max_length=200)

class Cart(models.Model):
    items = models.ManyToManyField(Product, related_name='cart')
    user = models.ForeignKey(User, on_delete= models.CASCADE, related_name='cart')


class OrderState(models.Model):
    state = models.CharField(choices=order_state, max_length= 100)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="states")
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='ostates')
    buyer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='states')




