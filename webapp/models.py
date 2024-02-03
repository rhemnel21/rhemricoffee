from django.db import models

class CustomersInfo(models.Model):
    name = models.CharField(max_length=50)
    contact = models.CharField(max_length=15, blank=False)  # Changed to CharField for flexibility
    email = models.EmailField(max_length=50)

    def __str__(self):
        return self.name


class Product(models.Model):
    customer_info = models.ForeignKey(CustomersInfo, on_delete=models.SET_NULL, null=True)
    item_name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(max_length=100)

    def __str__(self):
        return self.item_name

class Order(models.Model):
    name = models.CharField(max_length=255, null=True)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    size = models.CharField(max_length=1, null=True)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        if self.product:
            return f"{self.quantity} {self.size} {self.product.item_name} for {self.name}"
        else:
            return f"{self.quantity} {self.size} (No product set) for {self.name}"
    
class OrderDetail(models.Model):
    customer_info = models.ForeignKey(CustomersInfo, on_delete=models.SET_NULL, null=True)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    quantity = models.PositiveIntegerField(default=1)  # Default quantity is 1, not a boolean
    subtotal = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return str(self.quantity)

class Transaction(models.Model):
    customer_info = models.ForeignKey(CustomersInfo, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    payment_method = models.CharField(max_length=50)
    transaction_date = models.DateField(auto_now_add=True)
    time = models.TimeField(auto_now_add=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.payment_method
