from dash import Dash, html
import dash_cytoscape as cyto
import numpy as np
import pandas as pd

import platform

if platform.system() == 'Windows':
    fol = 'mts hack/'
else:
    fol = './'

df=pd.read_csv(fol+'00.csv')
df.columns = ['Подразделение 1', 'Функциональный блок', 'Подразделение 2',
       'Подразделение 3', 'Подразделение 4', 'Должность', 'Роль', 'Фамилия',
       'Имя', 'Телефон', 'Город', 'Адрес', 'Почта']


df['Имя']=df[['Имя','Фамилия']].apply(lambda x: ' '.join(x), axis=1)
df = df[['Подразделение 1', 'Функциональный блок', 'Подразделение 2',
       'Подразделение 3', 'Подразделение 4', 'Имя']].drop_duplicates()

elements=[]
ised =[]
for eow in np.array(df):
    eow = [i for i in eow if i is not np.nan]
    for i in range(len(eow)-1):

        if '/'.join(eow[:i+1]) not in ised:
            elements +=[        
                    {'data': {'id': '/'.join(eow[:i+1]), 'label': eow[i],'size':8-len(eow[:i+1])}}]
                    
        if '/'.join(eow[:i+2]) not in ised:
            elements +=[
                    {'data': {'id': '/'.join(eow[:i+2]), 'label': eow[i+1],'size':8-len(eow[:i+2])}}, 
                    {'data': {'source': '/'.join(eow[:i+1]), 'target': '/'.join(eow[:i+2])}}]
            
        ised +=['/'.join(eow[:i+1]),'/'.join(eow[:i+2])]

app = Dash(__name__)
print(elements)

app.layout = html.Div([
    cyto.Cytoscape(
        id='cytoscape',
        elements=elements,
        layout={
            'name': 'cose'
        },
        stylesheet=[
             {
                'selector': 'node',
                'style': {
                    'label': 'data(label)',
                    'background-color': '#FF4136'
                    
                }}]+[{'selector': f'[size ={i} ]',
                    'style': {
                        'background-color': '#FF4136',
                        'width': f"{100*i**1.5/7}%",
                        'height': f"{100*i**1.5/7}%"}
                } for i in range(0,7)],
        style={'width': '2900px', 'height': '600px'}
    )
])

if __name__ == '__main__':
    
    
    import platform

    if platform.system() == 'Windows':
        app.run_server(debug=False)
    else:
        app.run_server(host='0.0.0.0', port=8080)
