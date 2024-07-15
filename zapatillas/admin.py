from django.contrib import admin

from .models import Zapatilla

admin.site.register(Zapatilla)
class ZapatillaAdmin(admin.ModelAdmin):
    list_display = ('id_zapatilla', 'nombre', 'color', 'precio')  # Campos a mostrar en la lista
    actions = ['eliminar_zapatillas']  # Lista de acciones personalizadas

    def eliminar_zapatillas(self, request, queryset):
        queryset.delete()
    eliminar_zapatillas.short_description = "Eliminar zapatillas seleccionadas"
