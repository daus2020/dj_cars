from django.urls import path
from .views import addVehiculo, registroView, loginView, listarVehiculo, logoutView
from . import views
# from . import views  <-- do the same of line above

urlpatterns = [

    path('add/', addVehiculo, name='addVehiculo'),
    # path('vehiculo/add/', addVehiculo, name='addVehiculo'),
    path('listar/', listarVehiculo, name='listar'),
    # path('vehiculo/listar/', listarVehiculo, name='listar'),
    path('registro/', registroView, name='registro'),
    # path('vehiculo/registro/', registroView, name='registro'),
    path('login/', loginView, name='login'),
    # path('vehiculo/login/', loginView, name='login'),
    path('logout/', logoutView, name='logout'),
    # path('vehiculo/logout/', logoutView, name='logout'),
]
