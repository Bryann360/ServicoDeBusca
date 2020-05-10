from django.db import models

class Produto(models.Model):
    descricao = models.CharField(max_length=200)
    titulo = models.CharField
    imagem = models.CharField

    def __str__(self):
        return self.descricao

