from django.db import models

# Create your models here.
class Product(models.Model):
  type_choices = [
    ('p', 'Producto'),
    ('s', 'Servicio'),
    ('o', 'Otro'),
  ]

  #basic product information
  bar_code = models.CharField(
    max_length=20, 
    null=False, 
    blank=False, 
    unique=True)
  int_code = models.CharField(
    max_length=20, 
    null=False, 
    blank=False, 
    unique=True)
  description = models.CharField(max_length=200, null=False, blank=False)
  cost = models.FloatField(null=False, blank=False)
  last_cost = models.FloatField(null=True, blank=True)
  price = models.FloatField(null=False, blank=False)
  last_price = models.FloatField(null=True, blank=True)

  #product info for base products
  product_type = models.CharField(
    max_length=1, 
    choices=type_choices, 
    default='p')
  active = models.BooleanField(default=True, null=False, blank=False)
  saleable = models.BooleanField(default=True, null=False, blank=False)

  #history
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  #ForeignKey's
  category = models.ForeignKey(
    "Category", 
    on_delete=models.PROTECT, 
    null=False, 
    blank=False)

  class Meta:
    ordering = ('int_code',)
  
  def __str__(self):
    return ('[' + self.int_code + '] ' + self.description)

class Category(models.Model):
  class Meta:
    verbose_name_plural = 'Categories'

  name = models.CharField(max_length=15, unique=True, null=False, blank=False)
  active = models.BooleanField(default=True, null=False, blank=False)

  #history
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  def __str__(self):
    return self.name

