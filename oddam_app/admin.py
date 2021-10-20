from django.contrib import admin
from .models import Institution, Donation, Category
# Register your models here.


class InstitutionAdmin(admin.ModelAdmin):
    list_filter = ("type",)
    list_display = ("name", "type",)


class DonationAdmin(admin.ModelAdmin):
    list_filter = ("user", "institution", "city", )
    list_display = ("user", "city", "quantity", "institution")


admin.site.register(Institution, InstitutionAdmin)
admin.site.register(Donation, DonationAdmin)
admin.site.register(Category)
