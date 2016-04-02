import factory
from estabelecimento.models import *

class EstabelecimentoFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Estabelecimento

    nome = "TEISHOKU"

class ClienteFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Cliente

    cpf = "04341521101"


class PromocaoFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Promocao

    nome = "JUNTE 10 CARIMBOS E GANHE UM RODIZIO SIMPLES"
    quantidade_necessaria = 10
    premio = "RODIZIO SIMPLES"
    estabelecimento = factory.SubFactory(EstabelecimentoFactory)

class PremioFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Premio

    promocao = factory.SubFactory(PromocaoFactory)
    quem = factory.SubFactory(ClienteFactory)
