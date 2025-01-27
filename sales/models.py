from django.db import models


# Create your models here.
class Customer(models.Model):
    # first_name = models.CharField(max_length=30, error_messages="hoppla", help_text="max 30 letters, dummy")
    first_name = models.CharField(max_length=30, error_messages="hoppla", help_text="max 30 letters, dummy")
    last_name = models.CharField(max_length=30)
    newsletter_abo = models.BooleanField(default=True)
    email_address = models.CharField(max_length=30, blank=True, default="")
    account = models.FloatField(blank=True, null=True)
    # slug = models.SlugField(blank=True, default="")
    # one-to-many Order

    # class Meta:
    #     verbose_name = "Kunde"
    #     verbose_name_plural = "Kunden"
    #     ordering = ["-first_name"]

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    # def save(self, *args, **kwargs):
    #     print(f"new first name {self.first_name} has been saved")
    #     super().save(*args, **kwargs)


class Product(models.Model):
    name = models.CharField(max_length=30)
    price = models.FloatField()

    def __str__(self):
        return f"{self.name} ({self.price})"


class Bill(models.Model):
    total_amount = models.FloatField()
    is_paid = models.BooleanField(default=False)


class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    # many-to-one Customer

    products = models.ManyToManyField(Product, through="Producttype")
    # many-to-many Product

    bill = models.OneToOneField(Bill, on_delete=models.CASCADE)
    # one-to-one Bill


class Producttype(models.Model):
    type_name = models.CharField(max_length=30)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.type_name}"

