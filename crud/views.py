# crud/views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import Registro
from .forms import RegistroForm
from django.core.paginator import Paginator

def listar_registros(request):
    registros_list = Registro.objects.all().order_by('-id')
    paginator = Paginator(registros_list, 5)
    page = request.GET.get('page')
    registros = paginator.get_page(page)
    return render(request, 'crud/list.html', {'registros': registros})

def criar_registro(request):
    form = RegistroForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('listar_registros')
    return render(request, 'crud/form.html', {'form': form})

def editar_registro(request, pk):
    registro = get_object_or_404(Registro, pk=pk)
    form = RegistroForm(request.POST or None, instance=registro)
    if form.is_valid():
        form.save()
        return redirect('listar_registros')
    return render(request, 'crud/form.html', {'form': form})

def excluir_registro(request, pk):
    registro = get_object_or_404(Registro, pk=pk)
    if request.method == 'POST':
        registro.delete()
        return redirect('listar_registros')
    return render(request, 'crud/confirm_delete.html', {'registro': registro})
