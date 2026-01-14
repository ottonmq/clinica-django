from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.core import serializers
from .models import Paciente




def dashboard(request):
    conteo_p = Paciente.objects.count()
    # Pasamos total_p y total_c (usando el mismo conteo por ahora)
    return render(request, 'dashboard.html', {
        'total_p': conteo_p, 
        'total_c': conteo_p
    })

@login_required
def list_pacientes(request):
    pacientes = Paciente.objects.all()
    return render(request, 'list_pacientes.html', {'pacientes': pacientes})


@login_required
def form_paciente(request, pk=None):
    p = get_object_or_404(Paciente, pk=pk) if pk else None
    if request.method == 'POST':
        datos = {
            'nombre': request.POST.get('nombre'),
            'edad': request.POST.get('edad') or None,
            'nacionalidad': request.POST.get('nacionalidad'),
            'dui': request.POST.get('dui'),
            'telefono': request.POST.get('telefono'),
            'correo': request.POST.get('correo'),
            'direccion': request.POST.get('direccion'),
            'consulta_por': request.POST.get('consulta_por'),
            'enfermedad_actual': request.POST.get('enfermedad_actual'),
            'antecedentes_personales_familiares': request.POST.get('antecedentes_personales_familiares'),
            'pa': request.POST.get('pa'),
            'fc': request.POST.get('fc'),
            'fr': request.POST.get('fr'),
            'fum': request.POST.get('fum') or None,
            'fpm': request.POST.get('fpm') or None,
            'fpp': request.POST.get('fpp') or None,
            'amenorrea_semanas': request.POST.get('amenorrea_semanas') or 0,
            'amenorrea_dias': request.POST.get('amenorrea_dias') or 0,
            'tipo_ultrasonido': request.POST.get('tipo_ultrasonido'),
            'detalle_ultrasonido': request.POST.get('detalle_ultrasonido'),
        }
        if p:
            for clave, valor in datos.items(): setattr(p, clave, valor)
            p.save()
        else:
            Paciente.objects.create(**datos)
        return redirect('list_pacientes')
    return render(request, 'form_pacientes.html', {'p': p})


@login_required
def backup(request):
    data = serializers.serialize("json", Paciente.objects.all())
    response = HttpResponse(data, content_type="application/json")
    response['Content-Disposition'] = 'attachment; filename="backup.json"'
    return response

# ESTA FUNCIÓN ES LA QUE TE FALTA Y CAUSA EL ERROR

# AGREGA ESTO AL FINAL:
def base(request):
    return render(request, 'base.html')


def imprimir_paciente(request, pk):
    paciente = get_object_or_404(Paciente, pk=pk)
    return render(request, 'imprimir_paciente.html', {'p': paciente})


def eliminar_paciente(request, pk):
    paciente = get_object_or_404(Paciente, pk=pk)
    paciente.delete()
    return redirect('list_pacientes')
