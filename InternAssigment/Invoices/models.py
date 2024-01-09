from django.db import models

# Create your models here.

class Invoices(models.Model):
    Date = models.DateField()
    CustomerName=models.CharField(max_length=100)

    def __str__(self):
        return f"{self.CustomerName}"


class InvoicesDetails(models.Model):
    invoices = models.ForeignKey(Invoices,on_delete=models.CASCADE,null=True)
    description = models.CharField(max_length=255)
    quantity = models.PositiveIntegerField()
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    price = models.DecimalField(max_digits=10, decimal_places=2, editable=False)

    def __str__(self):
        return f"{self.invoices}"

    def save(self, *args, **kwargs):
        # Automatically calculate the price before saving
        self.price = self.quantity * self.unit_price
        super().save(*args, **kwargs)



