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

sql_query = "Select estrato, avg(punt_competencias_ciudadanas) as puntaje from familia join (Select * from estudiante join prueba on estudiante.id = prueba.id_estu) as pe on pe.id = familia.id_estu group by estrato order by avg(punt_competencias_ciudadanas) desc;"

df =pd.read_sql(sql_query, conn)

app =dash.Dash()
app.layout = html.Div([
    html.H1('Entrega 3', style={'text-align' : 'center'}),
    dcc.Graph(
        id = 'sample-graph',
        figure = px.bar(df[['estrato','puntaje']], x='estrato', y='puntaje', title='Relación estrato - Puntaje competencias ciudadanas').update_layout(
            xaxis_title = 'Estrato',
            yaxis_title = 'Puntaje competencias ciudadanas'
            )

        )
    ])


conn.close()

if __name__ == '__main__' :
    app.run_server(port=8085)