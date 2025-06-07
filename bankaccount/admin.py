from django.contrib import admin
from .models import BankAccount

# Register your models here.


class BankAccountAdmin(admin.ModelAdmin):
    list_display = ['user', 'account_number', 'balance', 'created_at', 'is_active']
    readonly_fields = ['account_number']
    list_filter = ['is_active']

admin.site.register(BankAccount, BankAccountAdmin)