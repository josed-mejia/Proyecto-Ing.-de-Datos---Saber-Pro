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

sql_query = "Select tiene_internet, punt_razonamiento_cuantitativo as puntaje from familia join (Select * from estudiante join prueba on estudiante.id = prueba.id_estu) as pe on pe.id = familia.id_estu;"

df =pd.read_sql(sql_query, conn)

app =dash.Dash()
app.layout = html.Div([
    html.H1('Entrega 3', style={'text-align' : 'center'}),
    dcc.Graph(
        id = 'sample-graph',
        figure = px.violin(df[['tiene_internet','puntaje']], x='tiene_internet', box=True, y='puntaje',  title='Relación tiene internet - Puntaje razonamiento cuantitativo').update_layout(
            xaxis_title = 'Tiene internet',
            yaxis_title = 'Puntaje razonamiento cuantitativo'
            )

        )
    ])


conn.close()

if __name__ == '__main__' :
    app.run_server(port=8085)