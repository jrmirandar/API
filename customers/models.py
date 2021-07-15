from django.db import models

class Contact(models.Model):
    name = models.CharField(blank=False, null=False, max_length=40)
    phone = models.CharField(blank=False, null=False, max_length=40)
    birth_date = models.DateField(blank=True, null=True)
    active = models.BooleanField(null=False, blank=False, default=True)

    #history
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return (self.name + ' [' + self.phone + ']')

class Customer(models.Model):
    name = models.CharField(blank=False, null=False, max_length=40)
    last_name = models.CharField(blank=True, null=True, max_length=40)
    is_company = models.BooleanField(blank=False, null=False)
    nit = models.CharField(blank=False, null=False, max_length=16, unique=True)
    adress = models.CharField(blank=True, null=True, max_length=200, default="CIUDAD")
    discont = models.IntegerField(null=False, default=0)
    credit_limit = models.FloatField(null=False, default=0.00)
    credit_days = models.IntegerField(null=False, default=0)
    email = models.EmailField(null=True, blank=True)
    active = models.BooleanField(null=False, blank=False, default=True)

    contacts = models.ManyToManyField(Contact, blank=True, related_name='contacts')

    #history
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ('nit',)

    def __str__(self):
        return ('[' + self.nit + '] ' + ((self.name) if self.is_company else (self.last_name + ', ' + self.name)))