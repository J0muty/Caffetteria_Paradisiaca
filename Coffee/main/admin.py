from django.contrib import admin
from .models import RegUser, MenuItem, Order


@admin.register(RegUser)
class RegUserAdmin(admin.ModelAdmin):
    list_display = (
        'email',
        'firstname',
        'lastname',
        'birthdate',
        'display_is_active',
        'display_is_staff',
        'display_dark_mode'
    )
    list_filter = ('is_active', 'is_staff', 'dark_mode', 'birthdate')
    search_fields = ('email', 'firstname', 'lastname')
    ordering = ('email',)

    @staticmethod
    def display_is_active(obj):
        print(f"Active: {obj.is_active}")
        return 'Да' if obj.is_active == 1 else 'Нет'


    @staticmethod
    def display_is_staff(obj):
        print(f"Staff: {obj.is_staff}")
        return 'Да' if obj.is_staff == 'True' else 'Нет'


    @staticmethod
    def display_dark_mode(obj):
        print(f"Dark Mode: {obj.dark_mode}")
        return 'Да' if obj.dark_mode == 'True' else 'Нет'

    readonly_fields = ('email',)

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        return form


@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'available')
    search_fields = ('name',)
    ordering = ('name',)


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('user', 'total_price', 'date', 'status')
    list_filter = ('status', 'date')
    ordering = ('-date',)
