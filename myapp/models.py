from django.db import models

class Mobile(models.Model):
    brand = models.CharField(max_length=100)  # Mobile brand (e.g., Samsung, Apple)
    model = models.CharField(max_length=100)  # Mobile model (e.g., Galaxy S21, iPhone 13)
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Price of the mobile phone
    image = models.ImageField(upload_to='mobile_images/', blank=True, null=True)  # Image field for mobile

    def __str__(self):
        return f"{self.brand} {self.model}"  # Return brand and model as string representation
