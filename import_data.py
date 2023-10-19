import os
import django
import pandas as pd

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
django.setup()

from polls.models import Question 

caminho_arquivo = 'C:\\Users\\luiza\\Documents\\mysite\\polls\\dados\\dados.xlsx'

if caminho_arquivo:
    df = pd.read_excel(caminho_arquivo, header=0)
    colunas_de_interesse = ['km', 'km final', 'km de Projeto', 'km final de Projeto', 'Status', 'Equipe/Empreiteira', 'Encontrado em', 'Executado em', 'Prazo', 'Sentido', 'Classe', 'Faixa', 'Rodovia', 'Origem', 'Código ARTESP', 'Cód interno', 'Lote', 'Comprimento(m)', 'Largura(m)', 'Observações', 'Recurso_1', 'Quantidade_1', 'Recurso_2', 'Quantidade_2', 'Caminho']
    df = df[colunas_de_interesse]
    dados = df.to_dict(orient='records')
    
    for dado in dados:
        nova_pergunta = Question(
            km=dado['km'],
            km_final=dado['km final'],
            km_de_projeto=dado['km de Projeto'],
            km_final_de_projeto=dado['km final de Projeto'],
            status=dado['Status'],
            empreiteira=dado['Equipe/Empreiteira'],
            encontrado_em=dado['Encontrado em'],
            executado_em=dado['Executado em'],
            prazo=dado['Prazo'],
            sentido=dado['Sentido'],
            classe=dado['Classe'],
            faixa=dado['Faixa'],
            rodovia=dado['Rodovia'],
            origem=dado['Origem'],
            codigo_artesp=dado['Código ARTESP'],
            codigo_interno=dado['Cód interno'],
            lote=dado['Lote'],
            comprimento=dado['Comprimento(m)'],
            largura=dado['Largura(m)'],
            observacoes=dado['Observações'],
            recurso_1=dado['Recurso_1'],
            quantidade_1=dado['Quantidade_1'],
            recurso_2=dado['Recurso_2'],
            quantidade_2=dado['Quantidade_2'],
            caminho=dado['Caminho']
        )
        nova_pergunta.save()

else:
    print("Nenhum arquivo selecionado.")
