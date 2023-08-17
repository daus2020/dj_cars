from django.contrib import admin
from django.urls import path, include
from vehiculo.views import IndexPageView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexPageView, name='index'),

    path('vehiculo/', include('vehiculo.urls')),
]
