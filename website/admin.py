from django.contrib import admin
from .models import Book

class CustomBookAdmin(admin.ModelAdmin):
    list_fields = ('Author','BookName','Editorial')
    search_fields = ['BookName']
 
admin.site.register(Book,CustomBookAdmin)
# Register your models here.
