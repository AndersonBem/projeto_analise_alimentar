from django.db import models
from django.contrib.auth.models import User

class Registro(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)  # Relaciona o registro ao usuário
    data = models.DateField()
    hora = models.TimeField()

    def __str__(self):
        return f"Registro {self.id} - {self.data} {self.hora}"

class ListaAlimentos(models.Model):
    nome = models.CharField(max_length=255)
    calorias_por_100g = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.nome

class AlimentosConsumidos(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)  # Usuário dono do consumo
    registro = models.ForeignKey(Registro, on_delete=models.CASCADE)
    alimento = models.ForeignKey(ListaAlimentos, on_delete=models.CASCADE)
    quantidade = models.DecimalField(max_digits=6, decimal_places=2)  # Quantidade em gramas

    def __str__(self):
        return f"{self.alimento.nome} - {self.quantidade}g"

class Pesagens(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    registro = models.ForeignKey(Registro, on_delete=models.CASCADE)
    peso = models.DecimalField(max_digits=5, decimal_places=2)  # Peso em kg

    def __str__(self):
        return f"Pesagem {self.peso} kg"

class DadosPessoais(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)  # Cada usuário tem um único perfil
    altura = models.DecimalField(max_digits=4, decimal_places=2)  # Altura em metros
    data_nascimento = models.DateField()

    def __str__(self):
        return self.usuario.username
