from django.contrib import admin
from .models import Resident, HouseResident


class HouseResidentInline(admin.TabularInline):
    model = HouseResident
    extra = 3


@admin.register(Resident)
class ResidentAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'lot_block', 'cpf',)
    inlines = [
        HouseResidentInline,
    ]
