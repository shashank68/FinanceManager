from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Stocks(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="stocks", null=False)

    Company_Name = models.TextField(max_length=100)
    Company_Symbol = models.TextField(max_length=50)
    Purchase_Date = models.DateField()
    Purchase_Cost = models.DecimalField(max_digits=7, decimal_places=3)
    Quantity = models.IntegerField()

    def __str__(self):
        return self.Company_Name

