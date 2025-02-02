from django.contrib import admin
from .models import Customer, Order, Product, Producttype, Bill

# Register your models here.


class CustomerAdmin(admin.ModelAdmin):
    list_filter = ["first_name", "last_name"]
    # list_display = ["last_name", "account"]
    # fields = ["first_name", "last_name"]
    # readonly_fields = ["account"]

    # prepopulated_fields = {
    #     "slug": ["first_name", "last_name"]
    # }

    fieldsets = [
        (
            None,
            {
                "fields": ["first_name", "last_name"]
            },
        ),
        (
            "Advanced tools",
            {
                "classes": ["collapse"],
                # "fields": ["slug", "account", "newsletter_abo"],
                "fields": ["account", "newsletter_abo"],

                "description": ["Hier findest du mehr Optionen"]
            }
        )
    ]


admin.site.register(Customer, CustomerAdmin)
admin.site.register(Order)
admin.site.register(Product)
admin.site.register(Producttype)
admin.site.register(Bill)
