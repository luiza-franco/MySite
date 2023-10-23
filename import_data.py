import pandas as pd
from polls.models import Question
from polls.models import Choice
import os
import django
import numpy as np

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")
django.setup()

def import_data(file_path):
    df = pd.read_excel(file_path)

    for _, row in df.iterrows():
        question = Question.objects.create(
            question_text=row['Question']
        )
        for i in range(1, len(df.columns) // 2 + 1): 
            choice_col = f'Choice {i}'
            votes_col = f'Votes {i}'

            answer_text = row[choice_col]
            votes = row[votes_col]
            if np.isnan(votes):
                votes = 0 #quando for nulo, gera 0


            choice = Choice.objects.create( #pega os objetos de models 
                question=question,
                choice_text=answer_text,
                votes=votes
            )



full_path = r"C:\Users\luiza\Documents\mysite\polls\dados\dados.xlsx"
import_data(full_path)