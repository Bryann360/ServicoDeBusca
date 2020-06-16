from django.db import models

class Produto(models.Model):
    titulo = models.CharField(max_length=200)
    descricao = models.CharField(max_length=200)
    imagem = models.CharField(max_length=200)
    foto = models.ImageField(max_length=200)

    

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




#alteraçoes no produto e esqueleto, foram adicionados imagem(preço) e foto(imagem do produto) 