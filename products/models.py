from django.db import models

CATEGORY_CHOICES = [
    ('womens', 'Womens'),
    ('mens', 'Mens'),
    ('kids', 'Kids'),
    ('brands', 'Brands'),
    ('offers', 'Offers'),
]

class Product(models.Model):
    name = models.CharField(max_length=255)
    brand = models.CharField(max_length=255)
    rating = models.IntegerField()
    msrp = models.IntegerField()
    price = models.IntegerField()
    colors = models.JSONField()  # list of color hex codes
    style = models.CharField(max_length=255, blank=True, null=True)  # 🟢 new
    size = models.CharField(max_length=255, blank=True, null=True)   # 🟢 new
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    image = models.ImageField(upload_to="products/", null=True, blank=True)

    def __str__(self):
        return self.name
