from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, PasswordChangeForm
from django.contrib.auth import login as auth_login, authenticate
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.db.models import Count
from django.db.models.functions import TruncMonth
from django.utils import timezone
from .models import Animal
from django.contrib.auth.decorators import login_required
from .forms import AnimalForm
from django.contrib.auth import logout
from django.contrib.auth import update_session_auth_hash


MESES = (
    "Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio",
    "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"
)


def index(request):
    animales = Animal.objects.filter(estado=Animal.ESTADO_DISPONIBLE)
    return render(request, 'index.html', {'animales': animales})


def contacto(request):
    return render(request, 'contacto.html')


def nosotros(request):
    return render(request, 'nosotros.html')


def loguearse(request):
    if request.method == 'GET':
        return render(request, 'loguearse.html', {
            'form': AuthenticationForm()
        })

    user = authenticate(
        request,
        username=request.POST['username'],
        password=request.POST['password']
    )

    if user is None:
        return render(request, 'loguearse.html', {
            'form': AuthenticationForm(),
            'error': 'Usuario o contraseña incorrectos'
        })

    auth_login(request, user)
    return redirect('index')


def registro(request):
    if request.method == 'GET':
        return render(request, 'registro.html', {
            'form': UserCreationForm()
        })

    if request.POST['password1'] == request.POST['password2']:
        try:
            user = User.objects.create_user(
                username=request.POST['username'],
                password=request.POST['password1']
            )
            user.save()
            auth_login(request, user)
            return redirect('index')

        except IntegrityError:
            return render(request, 'registro.html', {
                'form': UserCreationForm(),
                'error': 'El usuario ya existe'
            })

    return render(request, 'registro.html', {
        'form': UserCreationForm(),
        'error': 'Las contraseñas no coinciden'
    })


@login_required
def publicar_perro(request):
    if request.method == 'POST':
        form = AnimalForm(request.POST, request.FILES)
        if form.is_valid():
            animal = form.save(commit=False)
            animal.owner = request.user
            animal.estado = Animal.ESTADO_DISPONIBLE
            animal.save()
            return redirect('mis_publicaciones')
    else:
        form = AnimalForm()

    return render(request, 'publicar_perro.html', {'form': form})


def cerrar_sesion(request):
    logout(request)
    return redirect('index')


@login_required
def cambiar_password(request):
    if request.method == 'GET':
        return render(request, 'cambiar_password.html', {
            'form': PasswordChangeForm(request.user)
        })

    form = PasswordChangeForm(request.user, request.POST)

    if form.is_valid():
        user = form.save()
        update_session_auth_hash(request, user)
        return redirect('index')

    return render(request, 'cambiar_password.html', {
        'form': form,
        'error': 'Revisá los datos ingresados'
    })


@login_required
def mis_publicaciones(request):
    animales = Animal.objects.filter(owner=request.user).order_by('-id')
    return render(request, 'mis_publicaciones.html', {
        'animales': animales
    })


@login_required
def marcar_adoptado(request, animal_id):
    animal = get_object_or_404(
        Animal,
        id=animal_id,
        owner=request.user,
        estado=Animal.ESTADO_DISPONIBLE
    )

    if request.method == 'POST':
        animal.estado = Animal.ESTADO_ADOPTADO
        animal.fecha_adopcion = timezone.now()
        animal.save(update_fields=['estado', 'fecha_adopcion'])
        return redirect('mis_publicaciones')

    return render(request, 'confirmar_adopcion.html', {
        'animal': animal
    })


@login_required
def dar_baja_publicacion(request, animal_id):
    animal = get_object_or_404(
        Animal,
        id=animal_id,
        owner=request.user,
        estado=Animal.ESTADO_DISPONIBLE
    )

    if request.method == 'POST':
        animal.estado = Animal.ESTADO_BAJA
        animal.fecha_baja = timezone.now()
        animal.save(update_fields=['estado', 'fecha_baja'])
        return redirect('mis_publicaciones')

    return render(request, 'confirmar_baja.html', {
        'animal': animal
    })


@login_required
def editar_publicacion(request, animal_id):
    animal = get_object_or_404(
        Animal,
        id=animal_id,
        owner=request.user,
        estado=Animal.ESTADO_DISPONIBLE
    )

    if request.method == 'POST':
        form = AnimalForm(request.POST, request.FILES, instance=animal)

        if form.is_valid():
            form.save()
            return redirect('mis_publicaciones')
    else:
        form = AnimalForm(instance=animal)

    return render(request, 'editar_publicacion.html', {
        'form': form,
        'animal': animal
    })


def _clave_mes(fecha):
    return fecha.strftime('%Y-%m')


def _nombre_mes(fecha):
    return f"{MESES[fecha.month - 1]} {fecha.year}"


@login_required
def reportes(request):
    publicaciones_por_mes = (
        Animal.objects
        .filter(fecha_publicacion__isnull=False)
        .annotate(mes=TruncMonth('fecha_publicacion'))
        .values('mes')
        .annotate(cantidad=Count('id'))
        .order_by('mes')
    )

    adopciones_por_mes = (
        Animal.objects
        .filter(fecha_adopcion__isnull=False)
        .annotate(mes=TruncMonth('fecha_adopcion'))
        .values('mes')
        .annotate(cantidad=Count('id'))
        .order_by('mes')
    )

    bajas_por_mes = (
        Animal.objects
        .filter(fecha_baja__isnull=False)
        .annotate(mes=TruncMonth('fecha_baja'))
        .values('mes')
        .annotate(cantidad=Count('id'))
        .order_by('mes')
    )

    meses = {}

    for registro in publicaciones_por_mes:
        clave = _clave_mes(registro['mes'])
        meses.setdefault(clave, {
            'fecha': registro['mes'],
            'publicaciones': 0,
            'adopciones': 0,
            'bajas': 0,
        })
        meses[clave]['publicaciones'] = registro['cantidad']

    for registro in adopciones_por_mes:
        clave = _clave_mes(registro['mes'])
        meses.setdefault(clave, {
            'fecha': registro['mes'],
            'publicaciones': 0,
            'adopciones': 0,
            'bajas': 0,
        })
        meses[clave]['adopciones'] = registro['cantidad']

    for registro in bajas_por_mes:
        clave = _clave_mes(registro['mes'])
        meses.setdefault(clave, {
            'fecha': registro['mes'],
            'publicaciones': 0,
            'adopciones': 0,
            'bajas': 0,
        })
        meses[clave]['bajas'] = registro['cantidad']

    reporte_mensual = []
    for clave in sorted(meses.keys(), reverse=True):
        fila = meses[clave]
        fila['mes'] = _nombre_mes(fila['fecha'])
        if fila['publicaciones'] > 0:
            fila['tasa_adopcion'] = round(
                (fila['adopciones'] / fila['publicaciones']) * 100,
                1
            )
        else:
            fila['tasa_adopcion'] = None
        reporte_mensual.append(fila)

    total_publicaciones = Animal.objects.count()
    total_adoptados = Animal.objects.filter(estado=Animal.ESTADO_ADOPTADO).count()
    total_bajas = Animal.objects.filter(estado=Animal.ESTADO_BAJA).count()
    total_disponibles = Animal.objects.filter(estado=Animal.ESTADO_DISPONIBLE).count()
    historicos_sin_fecha = Animal.objects.filter(fecha_publicacion__isnull=True).count()

    tasa_adopcion_total = 0
    if total_publicaciones:
        tasa_adopcion_total = round((total_adoptados / total_publicaciones) * 100, 1)

    historial = Animal.objects.all().order_by('-fecha_publicacion', '-id')

    return render(request, 'reportes.html', {
        'reporte_mensual': reporte_mensual,
        'total_publicaciones': total_publicaciones,
        'total_adoptados': total_adoptados,
        'total_bajas': total_bajas,
        'total_disponibles': total_disponibles,
        'historicos_sin_fecha': historicos_sin_fecha,
        'tasa_adopcion_total': tasa_adopcion_total,
        'historial': historial,
    })
