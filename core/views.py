from django.shortcuts import render, redirect
from .forms import NomeVisitanteForm
from .models import Visitante


def home(request):
    visitante_id = request.session.get('visitante_id')
    visitante = None

    if visitante_id:
        try:
            visitante = Visitante.objects.get(id=visitante_id)
        except Visitante.DoesNotExist:
            visitante = None

    context = {
        'visitante': visitante
    }

    return render(request, 'core/home.html', context)


def coletar_nome_visitante(request):
    if request.method == 'POST':
        form = NomeVisitanteForm(request.POST)
        if form.is_valid():
            nome = form.cleaned_data['nome']
            visitante = Visitante.objects.create(nome=nome)
            request.session['visitante_id'] = str(visitante.id)
            return redirect('home')  # redireciona para home ou dashboard
    else:
        form = NomeVisitanteForm()
    return render(request, 'core/boas_vindas.html', {'form': form})

def sair_visitante(request):
    request.session.flush()
    return redirect('boas_vindas')