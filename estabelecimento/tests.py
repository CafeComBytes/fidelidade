from django.test import TestCase
from estabelecimento.factories import *
from estabelecimento.models import *

# Create your tests here.
class TesteDePromocao(TestCase):

    def testa_lancamento_de_duas_aquisicoes_em_uma_promocao(self):
        promocao = PromocaoFactory()
        quem = ClienteFactory()
        quantidade = 2

        promocao.lancar_aquisicao(quem, quantidade)

        aquisicoes = Aquisicao.objects.filter(promocao=promocao)
        self.assertEqual(len(aquisicoes), quantidade)
        self.assertEqual(list(map(lambda aquisicao: aquisicao.quem, aquisicoes)), [quem] * quantidade)
        self.assertEqual(list(map(lambda aquisicao: aquisicao.promocao, aquisicoes)), [promocao] * quantidade)

    def testa_lancamento_de_premio_quando_cliente_atinge_o_necessario_na_promocao(self):
        promocao = PromocaoFactory()
        quem = ClienteFactory()

        promocao.lancar_aquisicao(quem, promocao.quantidade_necessaria)

        premios = promocao.premios.all()
        self.assertEqual(1, len(premios))

    def testa_lancamento_de_multiplus_premios(self):
        promocao = PromocaoFactory()
        quem = ClienteFactory()

        promocao.lancar_aquisicao(quem, promocao.quantidade_necessaria * 2)

        self.assertEqual(2, promocao.premios.count())

class TesteDePremio(TestCase):
        def testa_utilizacao_de_um_premio(self):
            premio = PremioFactory()

            premio.utilizar()

            self.assertTrue(premio.foi_utilizado)
