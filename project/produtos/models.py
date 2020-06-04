from django.db import models

class Produto(models.Model):
    titulo = models.CharField(max_length=200)
    descricao = models.CharField(max_length=200)
    imagem = models.CharField
    foto = models.ImageField

    

    def __str__(self):
        return self.descricao


class Esqueleto():
    def __init__(self, nome, produto, preco, fotinho):
        self.titulo = nome
        self.link = produto
        self.imagem = preco
        self.foto = fotinho


    def __str__(self):
        return self.titulo