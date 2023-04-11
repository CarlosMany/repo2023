from django.shortcuts import render, redirect
from .models import Tarea, Tarea2
from .forms import TareaForm, Tarea2Form
# Create your views here.

def home(request):
    tareas = Tarea.objects.all()
    tareas2 = Tarea2.objects.all()
    context = {'tareas': tareas, 'tareas2': tareas2}
    return render(request, 'todo/home.html', context)

def agregar(request):
    if request.method == "POST":
        form = TareaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    else:
        form = TareaForm()
    context = {'form': form}
    return render(request, 'todo/agregar.html',context)

def agregar2(request):
    if request.method == "POST":
        form = Tarea2Form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    else:
        form = Tarea2Form()
    context = {'form': form}
    return render(request, 'todo/agregar.html',context)

def eliminar(request, tarea_id):
    tarea = Tarea.objects.get(id=tarea_id)
    tarea.delete()
    return redirect("home")

def eliminar2(request, tarea2_id):
    tarea2 = Tarea2.objects.get(id=tarea2_id)
    tarea2.delete()
    return redirect("home")

def editar(request, tarea_id):
    tarea = Tarea.objects.get(id=tarea_id)
    if request.method == "POST":
        form = TareaForm(request.POST, instance=tarea)
        if form.is_valid():
            form.save()
            return redirect("home")

    else:
        form = TareaForm(instance=tarea)
    context = {"form":form}
    return render(request,"todo/editar.html", context)

def editar2(request, tarea2_id):
    tarea2 = Tarea2.objects.get(id=tarea2_id)
    if request.method == "POST":
        form = Tarea2Form(request.POST, instance=tarea2)
        if form.is_valid():
            form.save()
            return redirect("home")

    else:
        form = Tarea2Form(instance=tarea2)
    context = {"form":form}
    return render(request,"todo/editar.html", context)


#//////////////////////////////////////


