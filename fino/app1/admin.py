from django.contrib import admin
from .models import Details
from .models import todolist
from .models import Transactions
from django.contrib.auth.models import Group

admin.site.site_header = 'FinM Dashboard'

class DetailsAdmin(admin.ModelAdmin):
    list_display = ('username','curbal', 'dail_el' , 'Today_ex', 'date')

# Register your models here.
admin.site.register(Details, DetailsAdmin)
admin.site.register(todolist)
admin.site.register(Transactions)
