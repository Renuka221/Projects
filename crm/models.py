from django.db import models
from datetime import date

class Customer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    gender = models.CharField(max_length=10)
    age = models.IntegerField()
    location = models.CharField(max_length=100)
    signup_date = models.DateField(default=date.today)
    last_active_date = models.DateField(default=date.today)
    total_spent = models.FloatField(default=0.0)
    is_churned = models.BooleanField(default=False)


    def __str__(self):
        return self.name

class ProductPurchase(models.Model):
    user = models.ForeignKey(Customer, on_delete=models.CASCADE, null=False)
    product_id = models.CharField(max_length=10)
    product_name = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    purchase_date = models.DateField()
    rating = models.IntegerField()

class CustomerMessage(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    message_text = models.TextField()
    sentiment_label = models.CharField(max_length=10)

class ChurnFeature(models.Model):
    customer = models.OneToOneField(Customer, on_delete=models.CASCADE)
    login_frequency = models.IntegerField()
    avg_session_time = models.FloatField()
    complaints_raised = models.IntegerField()
    last_purchase_days_ago = models.IntegerField()
    total_purchases = models.IntegerField()
