from django.contrib import admin
from django.contrib.auth.models import User, Permission

# Register your models here.
from .models import VehiculoModel

# admin.site.register(VehiculoModel)


@admin.register(VehiculoModel)
class VehiculoAdmin(admin.ModelAdmin):
    list_display = ('modelo', 'precio')


admin.site.unregister(User)


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'view_vehiculomodel', 'add_vehiculomodel')

    @admin.display(boolean=True)
    def add_vehiculomodel(self, obj):
        return obj.has_perm('vehiculo.add_vehiculomodel')

    @admin.display(boolean=True)
    def view_vehiculomodel(self, obj):
        return obj.has_perm('vehiculo.view_vehiculomodel')

    # def get_form(self, request, obj=None, **kwargs):
    #     form = super().get_form(request, obj, **kwargs)
    #     is_superuser = request.user.is_superuser
    #     if not is_superuser:
    #         form.base_fields['username'].disabled = True
    #     return form
