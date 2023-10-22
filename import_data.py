import pandas as pd
from polls.models import Question
import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")
django.setup()

def import_data(file_path):
    df = pd.read_excel(file_path)

    for _, row in df.iterrows():
        question = Question.objects.create(
            question_text=row['Question']
        )

file_path = r'C:\Users\luiza\Documents\mysite\polls\dados\dados.xlsx'
import_data(file_path)

