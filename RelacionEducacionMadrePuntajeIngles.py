import pandas as pd
import psycopg2 as psy2
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px

dbname = "Icfes"
user = "taylor"
password = "1234"
host = "localhost"

conn = psy2.connect(dbname = dbname, user = user, password = password, host = host)

sql_query = "Select educacion_madre, avg(punt_ingles) as puntaje from familia join (Select * from estudiante join prueba on estudiante.id = prueba.id_estu) as pe on pe.id = familia.id_estu group by educacion_madre order by avg(punt_ingles) desc;"

df =pd.read_sql(sql_query, conn)

app =dash.Dash()
app.layout = html.Div([
    html.H1('Entrega 3', style={'text-align' : 'center'}),
    dcc.Graph(
        id = 'sample-graph',
        figure = px.bar(df[['educacion_madre','puntaje']], x='educacion_madre', y='puntaje', title='Relación Educacion madre - Puntaje Ingles').update_layout(
            xaxis_title = 'Educacion madre',
            yaxis_title = 'Puntaje Ingles'
            )

        )
    ])


conn.close()

if __name__ == '__main__' :
    app.run_server(port=8085)