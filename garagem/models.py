from django.db import models

class Marca(models.Model):
    nome = models.CharField(max_length=50) 
    nacionalidade = models.CharField(null=True, blank=True, max_length=50 )

    def __str__(self):
        return f"{self.nome.upper()} ({self.id})"

class Categoria(models.Model):
    descricao = models.CharField(max_length=100)

    def __str__(self):
        return self.descricao
    
class Acessorio(models.Model):
    descricao = models.CharField(max_length=100)

    def __str__(self):
        return self.descricao
    
class Cor(models.Model):
     descricao = models.CharField(max_length=100)
     
     def __str__(self):
        return self.descricao
     
     class Meta:
        verbose_name_plural = "cores"
     
class Veiculo(models.Model):
    marca = models.ForeignKey(Marca, on_delete=models.PROTECT)
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT)
    cor = models.ForeignKey(Cor, on_delete=models.PROTECT)
    ano = models.IntegerField(null=True, default=0)
    preco = models.DecimalField(max_digits=10, decimal_places=2, null=True, default=0)
    modelo = models.CharField(max_length=50)

    def __str__(self):
        return f"Modelo: {self.modelo} (Cor: {self.cor} - Ano: {self.ano} - Marca: {self.marca})"  
      
    class Meta:
        verbose_name = "veículo"
    