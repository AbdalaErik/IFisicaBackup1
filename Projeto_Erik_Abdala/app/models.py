from django.db import models

# Create your models here.

class Area(models.Model):

    nome = models.CharField(max_length = 80)
    descricao = models.CharField(max_length = 300)

    def __str__(self):

        return f'{self.nome}'
    
class Subarea(models.Model):

    nome = models.CharField(max_length = 80)
    descricao = models.CharField(max_length = 300)
    area = models.ForeignKey(Area, on_delete = models.CASCADE)

    def __str__(self):

        return f'Subárea: {self.nome} Área: {self.area}'
    
class Topico(models.Model):

    nome = models.CharField(max_length = 80)
    descricao = models.CharField(max_length = 500)
    subarea = models.ForeignKey(Subarea, on_delete = models.CASCADE)

    def __str__(self):

        return f'{self.nome} {self.descricao} {self.subarea}'
    
class Fisico(models.Model):

    nome = models.CharField(max_length = 80)
    descricao = models.CharField(max_length = 300)
    data_nascimento = models.DateField()

    def __str__(self):

        return f'{self.nome} {self.descricao} {self.data_nascimento}'
    
class Invencao(models.Model):

    nome = models.CharField(max_length = 80)
    ano = models.DateField()
    fisico = models.ManyToManyField(Fisico)
    area = models.ManyToManyField(Area)

    def __str__(self):

        return f'{self.nome} {self.ano} {self.fisico} {self.area}'
    
class Questionario(models.Model):

    titulo = models.CharField(max_length = 80)
    descricao = models.CharField(max_length = 300)
    area = models.ForeignKey(Area, on_delete = models.CASCADE)

    def __str__(self):

        return f'{self.titulo} {self.descricao} {self.area}'
    
class Questao(models.Model):

    questionario = models.ForeignKey(Questionario, on_delete = models.CASCADE)
    titulo = models.CharField(max_length = 80)
    enunciado = models.CharField(max_length = 500)
    alternativa_a = models.CharField(max_length = 300)
    alternativa_b = models.CharField(max_length = 300)
    alternativa_c = models.CharField(max_length = 300)
    alternativa_d = models.CharField(max_length = 300)
    alternativa_e = models.CharField(max_length = 300)
    alternativa_correta = models.CharField(max_length = 1)
    alternativa_submetida = models.CharField(max_length = 1, blank = True, null = True)

    def __str__(self):

        return f'{self.titulo} {self.enunciado} {self.alternativa_a}' \
        f'{self.alternativa_b} {self.alternativa_c} {self.alternativa_d}' \
        f'{self.alternativa_e} {self.alternativa_correta}' \
        f'{self.alternativa_submetida}'
    
class Ocupacao(models.Model):

    nome = models.CharField(max_length = 30)

    def __str__(self):

        return self.nome
    
class Pessoa(models.Model):

    nome = models.CharField(max_length = 80)
    email = models.CharField(max_length = 50)
    ocupacao = models.ForeignKey(Ocupacao, on_delete = models.CASCADE)

    def __str__(self):

        return f'{self.nome} {self.email} {self.ocupacao}'
    
class QuestionarioRespondido(models.Model):

    questionario = models.ForeignKey(Questionario, on_delete = models.CASCADE)
    pessoa = models.ForeignKey(Pessoa, on_delete = models.CASCADE)
    data_realizacao = models.DateTimeField()
    numero_acertos = models.PositiveIntegerField()

    def __str__(self):

        return f'{self.questionario} {self.pessoa} {self.data_realizacao} {self.numero_acertos}'