from django.contrib import admin
from .models import Invoices,InvoicesDetails

# Register your models here.

@admin.register(Invoices)
class InvoicesAdmin(admin.ModelAdmin):
    list_display = ['id','Date','CustomerName']

@admin.register(InvoicesDetails)
class InvoicesDetailsAdmin(admin.ModelAdmin):
    list_display = ['id','invoices','description','quantity','unit_price','price']



