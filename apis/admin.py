from django.contrib import admin
from .models import *

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ["name","phone","email","created_at",]   
    list_filter = ["name","email","created_at",]
    search_fields = ["name","email","user"]


@admin.register(Wallet)
class WalletAdmin(admin.ModelAdmin):
    list_display = ["customer","balance",]   
    list_filter = ["customer","balance",]
    search_fields = ["customer","balance",]


@admin.register(Loan)
class LoanAdmin(admin.ModelAdmin):
    list_display = ["customer","total_amount",]   
    list_filter = ["customer","total_amount",]
    search_fields = ["customer","total_amount",]


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ["loan","amount","description",]   
    list_filter = ["loan","amount","description",]
    search_fields = ["loan","amount","description",]