from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound
from .models import Experiencia, Aprendiz, Mentor, Actividad, NivelDeAprendizaje
from .forms import ExperienciaForm, AprendizForm, MentorForm, ActividadForm, NivelDeAprendizajeForm

# Vistas para Experiencia

def inicio(request):
    return render(request, 'myapp1/index.html')

def experiencia_list(request):
    experiencias = Experiencia.objects.all()
    return render(request, 'myapp1/experiencia_list.html', {'experiencias': experiencias})


def experiencia_detail(request, pk):
    try:
        experiencia = Experiencia.objects.get(pk=pk)
    except Experiencia.DoesNotExist:
        return HttpResponseNotFound("Experiencia no encontrada")
    return render(request, 'myapp1/experiencia_detail.html', {'experiencia': experiencia})

def experiencia_create(request):
    if request.method == "POST":
        form = ExperienciaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('experiencia_list')
    else:
        form = ExperienciaForm()
    return render(request, 'myapp1/experiencia_form.html', {'form': form, 'title': 'Crear Experiencia'})

def experiencia_update(request, pk):
    try:
        experiencia = Experiencia.objects.get(pk=pk)
    except Experiencia.DoesNotExist:
        return HttpResponseNotFound("Experiencia no encontrada")
    
    if request.method == "POST":
        form = ExperienciaForm(request.POST, instance=experiencia)
        if form.is_valid():
            form.save()
            return redirect('experiencia_list')
    else:
        form = ExperienciaForm(instance=experiencia)
    return render(request, 'myapp1/experiencia_form.html', {'form': form, 'title': 'Actualizar Experiencia'})

def experiencia_delete(request, pk):
    try:
        experiencia = Experiencia.objects.get(pk=pk)
    except Experiencia.DoesNotExist:
        return HttpResponseNotFound("Experiencia no encontrada")
    
    if request.method == "POST":
        experiencia.delete()
        return redirect('experiencia_list')
    return render(request, 'myapp1/experiencia_confirm_delete.html', {'experiencia': experiencia})

# Vistas para Aprendiz

def aprendiz_list(request):
    aprendices = Aprendiz.objects.all()
    return render(request, 'myapp1/aprendiz_list.html', {'aprendices': aprendices})

def aprendiz_detail(request, pk):
    try:
        aprendiz = Aprendiz.objects.get(pk=pk)
    except Aprendiz.DoesNotExist:
        return HttpResponseNotFound("Aprendiz no encontrado")
    return render(request, 'aprendiz_detail.html', {'aprendiz': aprendiz})

def aprendiz_create(request):
    if request.method == "POST":
        form = AprendizForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('aprendiz_list')
    else:
        form = AprendizForm()
    return render(request, 'myapp1/aprendiz_form.html', {'form': form, 'title': 'Crear Aprendiz'})

def aprendiz_update(request, pk):
    try:
        aprendiz = Aprendiz.objects.get(pk=pk)
    except Aprendiz.DoesNotExist:
        return HttpResponseNotFound("Aprendiz no encontrado")
    
    if request.method == "POST":
        form = AprendizForm(request.POST, instance=aprendiz)
        if form.is_valid():
            form.save()
            return redirect('aprendiz_list')
    else:
        form = AprendizForm(instance=aprendiz)
    return render(request, 'myapp1/aprendiz_form.html', {'form': form, 'title': 'Actualizar Aprendiz'})

def aprendiz_delete(request, pk):
    try:
        aprendiz = Aprendiz.objects.get(pk=pk)
    except Aprendiz.DoesNotExist:
        return HttpResponseNotFound("Aprendiz no encontrado")
    
    if request.method == "POST":
        aprendiz.delete()
        return redirect('aprendiz_list')
    return render(request, 'myapp1/aprendiz_confirm_delete.html', {'aprendiz': aprendiz})

# Vistas para Mentor

def mentor_list(request):
    mentores = Mentor.objects.all()
    return render(request, 'myapp1/mentor_list.html', {'mentores': mentores})

def mentor_detail(request, pk):
    try:
        mentor = Mentor.objects.get(pk=pk)
    except Mentor.DoesNotExist:
        return HttpResponseNotFound("Mentor no encontrado")
    return render(request, 'myapp1/mentor_detail.html', {'mentor': mentor})

def mentor_create(request):
    if request.method == "POST":
        form = MentorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('mentor_list')
    else:
        form = MentorForm()
    return render(request, 'myapp1/mentor_form.html', {'form': form, 'title': 'Crear Mentor'})

def mentor_update(request, pk):
    try:
        mentor = Mentor.objects.get(pk=pk)
    except Mentor.DoesNotExist:
        return HttpResponseNotFound("Mentor no encontrado")
    
    if request.method == "POST":
        form = MentorForm(request.POST, instance=mentor)
        if form.is_valid():
            form.save()
            return redirect('mentor_list')
    else:
        form = MentorForm(instance=mentor)
    return render(request, 'myapp1/mentor_form.html', {'form': form, 'title': 'Actualizar Mentor'})

def mentor_delete(request, pk):
    try:
        mentor = Mentor.objects.get(pk=pk)
    except Mentor.DoesNotExist:
        return HttpResponseNotFound("Mentor no encontrado")
    
    if request.method == "POST":
        mentor.delete()
        return redirect('mentor_list')
    return render(request, 'myapp1/mentor_confirm_delete.html', {'mentor': mentor})

# Vistas para Actividad

def actividad_list(request):
    actividades = Actividad.objects.all()
    return render(request, 'myapp1/actividad_list.html', {'actividades': actividades})

def actividad_detail(request, pk):
    try:
        actividad = Actividad.objects.get(pk=pk)
    except Actividad.DoesNotExist:
        return HttpResponseNotFound("Actividad no encontrada")
    return render(request, 'myapp1/actividad_detail.html', {'actividad': actividad})

def actividad_create(request):
    if request.method == "POST":
        form = ActividadForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('actividad_list')
    else:
        form = ActividadForm()
    return render(request, 'myapp1/actividad_form.html', {'form': form, 'title': 'Crear Actividad'})

def actividad_update(request, pk):
    try:
        actividad = Actividad.objects.get(pk=pk)
    except Actividad.DoesNotExist:
        return HttpResponseNotFound("Actividad no encontrada")
    
    if request.method == "POST":
        form = ActividadForm(request.POST, instance=actividad)
        if form.is_valid():
            form.save()
            return redirect('actividad_list')
    else:
        form = ActividadForm(instance=actividad)
    return render(request, 'myapp1/actividad_form.html', {'form': form, 'title': 'Actualizar Actividad'})

def actividad_delete(request, pk):
    try:
        actividad = Actividad.objects.get(pk=pk)
    except Actividad.DoesNotExist:
        return HttpResponseNotFound("Actividad no encontrada")
    
    if request.method == "POST":
        actividad.delete()
        return redirect('actividad_list')
    return render(request, 'myapp1/actividad_confirm_delete.html', {'actividad': actividad})

# Vistas para NivelDeAprendizaje

def nivel_list(request):
    niveles = NivelDeAprendizaje.objects.all()
    return render(request, 'myapp1/nivel_list.html', {'niveles': niveles})

def nivel_detail(request, pk):
    try:
        nivel = NivelDeAprendizaje.objects.get(pk=pk)
    except NivelDeAprendizaje.DoesNotExist:
        return HttpResponseNotFound("Nivel de Aprendizaje no encontrado")
    return render(request, 'myapp1/nivel_detail.html', {'nivel': nivel})

def nivel_create(request):
    if request.method == "POST":
        form = NivelDeAprendizajeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('nivel_list')
    else:
        form = NivelDeAprendizajeForm()
    return render(request, 'myapp1/nivel_form.html', {'form': form, 'title': 'Crear Nivel de Aprendizaje'})


def nivel_update(request, pk):
    try:
        nivel = NivelDeAprendizaje.objects.get(pk=pk)
    except NivelDeAprendizaje.DoesNotExist:
        return HttpResponseNotFound("Nivel de Aprendizaje no encontrado")
    
    if request.method == "POST":
        form = NivelDeAprendizajeForm(request.POST, instance=nivel)
        if form.is_valid():
            form.save()
            return redirect('nivel_list')
    else:
        form = NivelDeAprendizajeForm(instance=nivel)
    return render(request, 'myapp1/nivel_form.html', {'form': form, 'title': 'Actualizar Nivel de Aprendizaje'})

def nivel_delete(request, pk):
    try:
        nivel = NivelDeAprendizaje.objects.get(pk=pk)
    except NivelDeAprendizaje.DoesNotExist:
        return HttpResponseNotFound("Nivel de Aprendizaje no encontrado")
    
    if request.method == "POST":
        nivel.delete()
        return redirect('nivel_list')
    return render(request, 'myapp1/nivel_confirm_delete.html', {'nivel': nivel})
