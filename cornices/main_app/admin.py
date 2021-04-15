from django.contrib import admin

from .models import Contact, PriceList


class ContactModelAdmin(admin.ModelAdmin):
    list_display = ('phone_number', 'viber', 'email', 'address', 'NIP', 'REGON')


class PriceListModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')
    list_filter = ('price',)
    search_fields = ('name',)


admin.site.register(Contact, ContactModelAdmin)
admin.site.register(PriceList, PriceListModelAdmin)
