import datetime
from django.db import models
from django.urls import reverse

# Create your models here.
class Item(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    image = models.ImageField(upload_to = 'images/', default='images/icon-load-256x256.png')
    description = models.TextField(
        max_length=1000,
        help_text="Short description for the product",
        blank=True,
        null=True)
    def get_price(self):
        return f'${self.price}'
    def __str__(self) -> str:
        return self.name
    class Meta:
        ordering = ['name']

class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_death = models.DateField('Died', null=True, blank=True)

    class Meta:
        ordering = ['last_name', 'first_name']
    
    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'

class Book(Item):
    author = models.ManyToManyField('Author')
    language = models.CharField(max_length=100, blank=True, null=True)
    
    def __str__(self) -> str:
        return self.name
    def get_absolute_url(self):
        return reverse('book-detail', args=[str(self.id)])
    def get_authors(self):
        return ', '.join(au.__str__() for au in self.author.all()[:3])
    get_authors.short_description = 'Author'

class MobilePhone(Item):
    cpu = models.CharField(max_length=100, blank=True, null=True)
    RAM_CHOICES = (
        ('3', '3GB'),
        ('4', '4GB'),        
    )
    ram = models.CharField(max_length=1, choices=RAM_CHOICES, blank=True, null=True, default='3')
    STORAGE = (
        ('32', '32GB'),
        ('64', '64GB'),
        ('128', '128GB')
    )
    storage = models.CharField(max_length=10, choices=STORAGE, blank=True, null=True, default='32')

    def __str__(self) -> str:
        return f'{self.name} | {self.ram} | {self.storage}'
    def get_absolute_url(self):
        return reverse('mobile-detail', args=[str(self.id)])
    

class Laptop(Item):
    cpu = models.CharField(max_length=100, blank=True, null=True)
    RAM_CHOICES = (
        ('8', '8GB'),
        ('16', '16GB'),        
    )
    ram = models.CharField(max_length=2, choices=RAM_CHOICES, blank=True, null=True, default='8')
    STORAGE = (
        ('500', '500GB'),
        ('1000', '1TB'),
    )
    storage = models.CharField(max_length=10, choices=STORAGE, blank=True, null=True, default='500')

    def __str__(self) -> str:
        return f'{self.name} | {self.ram} | {self.storage}'
    def get_absolute_url(self):
        return reverse('laptop-detail', args=[str(self.id)])
    
class Cloth(Item):
    color = models.CharField(max_length=50)
    SIZE = (
        ('S', 'S'),
        ('M', 'M'),
        ('XL', 'XL'),
        ('XXL', 'XXL'),
    )
    size = models.CharField(max_length=3, choices=SIZE, default='M')

    def __str__(self) -> str:
        return f'{self.name} | {self.size}'
    def get_absolute_url(self):
        return reverse('cloth-detail', args=[str(self.id)])
    
class Shoe(Item):
    color = models.CharField(max_length=50)
    size = models.PositiveIntegerField()

    def __str__(self) -> str:
        return f'{self.name} | {self.size}'
    def get_absolute_url(self):
        return reverse('shoe-detail', args=[str(self.id)])
class Electronic(Item):
    pass    

class BuyedItem(models.Model):
    item = models.ForeignKey(Item, on_delete=models.SET_NULL, null=True)
    bill = models.ForeignKey('Bill', on_delete=models.CASCADE, null=True, blank=True)
    price = models.FloatField()
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self) -> str:
        return self.item.__str__()

class Bill(models.Model):
    customer = models.CharField(max_length=100, verbose_name="Customer name")
    address = models.CharField(max_length=200, help_text='Where do you want to receive this order?')
    tel = models.CharField(max_length=11)
    date = models.DateField(default=datetime.datetime.now())
    