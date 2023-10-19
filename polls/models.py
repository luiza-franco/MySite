
import datetime
from django.db import models
from django.utils import timezone

class Question(models.Model):
    km = models.FloatField(null=True, blank=True)
    km_final = models.FloatField(null=True, blank=True)
    km_de_projeto = models.FloatField(null=True, blank=True)
    km_final_de_projeto = models.FloatField(null=True, blank=True)
    status = models.CharField(max_length=100, null=True, blank=True)
    empreiteira = models.CharField(max_length=100)  #obrigatório
    encontrado_em = models.DateTimeField(null=True, blank=True)
    executado_em = models.DateTimeField(null=True, blank=True)
    prazo = models.DateTimeField(null=True, blank=True)
    sentido = models.CharField(max_length=100)  #obrigatório
    classe = models.CharField(max_length=100)  #obrigatório
    faixa = models.CharField(max_length=100)  #obrigatório
    rodovia = models.CharField(max_length=100)  #obrigatório
    origem = models.CharField(max_length=100, null=True, blank=True)
    codigo_artesp = models.CharField(max_length=100, null=True, blank=True)
    codigo_interno = models.CharField(max_length=100, null=True, blank=True)
    lote = models.CharField(max_length=100, null=True, blank=True)
    comprimento = models.FloatField(null=True, blank=True)
    largura = models.FloatField(null=True, blank=True)
    observacoes = models.TextField(null=True, blank=True)
    recurso_1 = models.CharField(max_length=100, null=True, blank=True)
    quantidade_1 = models.FloatField(null=True, blank=True)
    recurso_2 = models.CharField(max_length=100, null=True, blank=True)
    quantidade_2 = models.FloatField(null=True, blank=True)
    caminho = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
