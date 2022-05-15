from django.contrib import admin

from .models import Author, Bill, Book, BuyedItem, Laptop, MobilePhone, Cloth, Shoe

# Register your models here.

#admin.site.register(Author)
#admin.site.register(Book)
#admin.site.register(Laptop)
#admin.site.register(MobilePhone)
admin.site.register(Cloth)
admin.site.register(Shoe)

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'get_authors')

@admin.register(Laptop)
class LaptopAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'ram', 'storage')

@admin.register(MobilePhone)
class MobilePhoneAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'ram', 'storage')

admin.site.register(BuyedItem)

class BuyedItemInline(admin.TabularInline):
    model = BuyedItem
    extra = 0

@admin.register(Bill)
class BillAdmin(admin.ModelAdmin):
    list_display = ('customer', 'date', 'address', 'tel')
    inlines = [BuyedItemInline]