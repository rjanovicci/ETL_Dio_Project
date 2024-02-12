import pandas as pd
import json

df = pd.read_csv('SalariosAtuais.csv')

df['Salario'] = df['Salario'] * 1.05

data_dict = df.to_dict(orient='records')

with open('SalariosAjustados.json', 'w') as json_file:
    json.dump(data_dict, json_file, indent=2)
