from django.db import models

# Create your models here.
class Products(models.Model):
    ALL_PRODUCT_CATEGORIES = [
        ('Vegetables', 'vegetables'),
        ('Fruits', 'fruits'),
        ('Eggs', 'eggs'),
        ('Milk', 'milk'),
        ('Honey', 'honey'),
        ('Trees', 'trees'),
        ('Wheat', 'wheat'),
        ('Maize', 'maize')
    ]

    product_name = models.CharField(max_length=25)
    product_description = models.TextField()
    product_image_1 = models.ImageField(upload_to='.s/assets/images/')
    product_image_2 = models.ImageField(upload_to='.s/assets/images/')
    product_image_3 = models.ImageField(upload_to='.s/assets/images/')
    product_category = models.CharField(max_length=15,choices=ALL_PRODUCT_CATEGORIES)
    product_amount = models.CharField(max_length=30)
    available_location = models.CharField(max_length=30)
    date_posted = models.DateTimeField()

    class Meta: 
        ordering = ['date_posted']
