# Create your models here.
from django.db import models


class Shop(models.Model):
    """Model For Shop"""
    shop_name = models.CharField(max_length=100, null=True, blank=True)
    shop_location = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        """show the shop name in admin pannel"""
        return self.shop_name.__str__()


class Category(models.Model):
    """Model for the Category"""
    category_name = models.CharField(max_length=100, null=True, blank=True)
    parent_cat = models.IntegerField(null=True, blank=True)
    shop_id = models.ForeignKey(Shop, on_delete=models.CASCADE)

    def __str__(self):
        """show the category name"""
        return self.category_name.__str__()


class Product(models.Model):
    """Model for Product"""
    product_name = models.CharField(max_length=100, null=True, blank=True)
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        """show  the product name in admin pannel"""
        return self.product_name.__str__()


class Media(models.Model):
    """Model to store product image"""
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    product_image = models.ImageField(upload_to='product_image', default='product_image/no-image-icon.png')

    def __str__(self):
        """show  the product image name"""
        return self.product_image.name
