class Order(models.Model):
    STATUS_CHOICES = [
        ('PENDING','pending'),
        ('PREPARING', 'preparing'),
        ('DELIVERED', 'delivered'),
        ('CANCELLED', 'cancelled'),
    ]
    customer=models.ForeingKey(User,on_delete=models.CASCADE, related_name='orders')
    items=models.ManyToManyField(MenuItem,related_name='orders')
    total_amount=models.DecimalField(max_digits=8,decimal_places=2)
    status=models.CharField(max_length=20, CHOICES=STATUS_CHOICES,default='PENDING')
    def __str__(self):
        return f"Order #{self.id} by {self.customer.username}"
    
    def calculate_total(self):
        return sum(item.price for item in self.items.all())