from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from tokenize import PseudoExtras
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required, permission_required

# from django.views.generic import TemplateView

from .models import VehiculoModel
from .forms import VehiculoForm, RegistroUsuarioForm
from django.contrib.auth.models import Permission
# from django.contrib.contenttypes.models import ContentType
# from django.urls import reverse
# Create your views here.


# def IndexPageView(request):
#     return render(request, 'index.html')  <-- also works without {}

def IndexPageView(request):
    return render(request, 'index.html', {'navbar': 'index'})


# class IndexPageView(TemplateView):
#     template_name = "index.html"

# @login_required(login_url='login')
@login_required
@permission_required('vehiculo.add_vehiculomodel', login_url='login')
def addVehiculo(request):
    form = VehiculoForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        form = VehiculoForm()
        messages.success(request, 'Datos procesados exitosamente.')

    return render(request, 'addform.html', {'form': form,  'navbar': 'addform'})


def registroView(request):
    if request.method == 'POST':
        form = RegistroUsuarioForm(request.POST)
        if form.is_valid():

            user = form.save()

            # user.user_permissions.add(visualizar_catalogo)

            login(request, user)
            messages.success(request, 'Usuario registrado exitosamente.')
            return redirect('listar')
        messages.error(request, 'Registro inválido. Verifique')

    form = RegistroUsuarioForm()
    context = {"register_form": form}
    return render(request, 'registro.html', context)


def loginView(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"Iniciaste sesión como: {username}.")
                return redirect('listar')
            else:
                messages.error(request, "Usuario y/o password inválido(s)")

    form = AuthenticationForm()
    context = {"login_form": form}
    return render(request, "login.html", context)
    # user = authenticate(username, password)


@login_required
def listarVehiculo(request):
    vehiculos = VehiculoModel.objects.all()
    context = {'lista_vehiculos': vehiculos, 'navbar': 'lista'}
    return render(request, "lista.html", context)


def logoutView(request):
    logout(request)
    messages.info(request, "Sesión cerrada exitosamente.")
    return HttpResponseRedirect('/')
