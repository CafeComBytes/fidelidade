from django.shortcuts import render
from estabelecimento.models import Promocao

def listar_promocoes(requisicao):
    promocoes = Promocao.objects.all()
    return render(requisicao, 'listar_promocoes.html', {"promocoes": promocoes})
