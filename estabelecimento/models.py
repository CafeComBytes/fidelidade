from django.db import models

class Estabelecimento(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Cliente(models.Model):
    cpf = models.CharField(max_length=11)

    def __str__(self):
        return self.cpf

class Aquisicao(models.Model):
    promocao = models.ForeignKey('Promocao')
    quem = models.ForeignKey(Cliente)
    quando = models.DateField(auto_now_add=True)

    def __str__(self):
        return "{0} - {1} - {2}".format(self.promocao, self.quem, self.quando)

class Promocao(models.Model):
    nome = models.CharField(max_length=100)
    premio = models.CharField(max_length=100)
    quantidade_necessaria = models.IntegerField()
    estabelecimento = models.ForeignKey(Estabelecimento)

    def lancar_aquisicao(self, quem, aquisicoes):
        for cada_aquisicao in range(aquisicoes):
            Aquisicao.objects.create(promocao=self, quem=quem)
            self.__premiar(quem)

    def __premiar(self, quem):
        deve_ganhar_premio = (Aquisicao.objects.filter(promocao=self, quem=quem).count() % self.quantidade_necessaria) == 0
        if deve_ganhar_premio:
            Premio.objects.create(promocao=self, quem=quem)

    def __str__(self):
        return self.nome

class Premio(models.Model):
    promocao = models.ForeignKey(Promocao, related_name="premios")
    quem = models.ForeignKey(Cliente)
    foi_utilizado =  models.BooleanField(default=False)

    def utilizar(self):
        self.foi_utilizado = True

    def __str__(self):
        return "{0} - {1} - {2} - {3}".format(self.quem, self.promocao, self.foi_utilizado, self.id)
