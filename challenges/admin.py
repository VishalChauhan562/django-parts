from django.contrib import admin
from .models import Month
# Register your models here.

@admin.register(Month)
class MonthAdmin(admin.ModelAdmin):
    list_display =['id','name','idea','position','isGoodIdea','slug','created_on','updated_on']
    prepopulated_fields = {"slug":("name",)}
    list_filter = ('position', 'isGoodIdea',
                   ('created_on', admin.DateFieldListFilter),
                   ('updated_on', admin.DateFieldListFilter))
