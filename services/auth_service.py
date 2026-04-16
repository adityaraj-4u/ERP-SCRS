import pandas as pd
from utils.file_handler import load_csv
from models.student import Student

def login(student_id):
    df = load_csv("data/students.csv")

    for _, row in df.iterrows():
        if str(row['id']).strip() == student_id.strip():

            if pd.notna(row['completed']):
                completed = str(row['completed']).split('|')
            else:
                completed = []

            return Student(row['id'], row['name'], row['program'], completed)

    return None