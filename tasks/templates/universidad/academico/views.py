from django.shortcuts import render, redirect
from .models import Curso
# Create your views here.

def home(request):
    cursos=Curso.objects.all()
    return render(request,"gestionCursos.html", {"cursos":cursos})

def registrarCurso(request):
    codigo=request.POST['txtCodigo']
    nombre=request.POST['txtNombre']
    creditos=request.POST['numCreditos']

    curso=Curso.objects.create(
        codigo=codigo, nombre=nombre, creditos=creditos)
    return redirect('/')