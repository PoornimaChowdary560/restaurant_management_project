from django.db import models
class MenuItem(models.Model):
    name=models.CharField(max_length=100)
    description=models.TextField(blank=True)
    price=models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.name

class RestaurantLocation(models.Model):
    address =models.CharField(max_length=255)
    city=models.CharField(max_length=100)
    state=models.CharField(max_length=100)
    zip_code=models.CharField(max_length=20)
    def __str__(self):
        return f"{self.address}, {self.city}, {self.state} - {self.zip_code}"

class ContactSubmission(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    submitted_at=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.name}-{self.email}"