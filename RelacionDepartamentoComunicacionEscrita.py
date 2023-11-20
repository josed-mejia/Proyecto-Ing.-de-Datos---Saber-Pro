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

sql_query = "Select departamento.nombre as departamento , avg(punt_comunicacion_escrita) as puntaje from departamento join (select * from municipio join (Select * from estudiante join prueba on estudiante.id = prueba.id_estu) as pe on pe.id_mun_res = municipio.id) as pem on pem.id_dept = departamento.id group by departamento.nombre order by avg(punt_comunicacion_escrita) desc;"

df =pd.read_sql(sql_query, conn)

app =dash.Dash()
app.layout = html.Div([
    html.H1('Entrega 3', style={'text-align' : 'center'}),
    dcc.Graph(
        id = 'sample-graph',
        figure = px.bar(df[['departamento','puntaje']], x='departamento', y='puntaje', title='Relación departamento - Puntaje comunicación escrita').update_layout(
            xaxis_title = 'Departamento',
            yaxis_title = 'Puntaje comunicación escrita'
            )

        )
    ])


conn.close()

if __name__ == '__main__' :
    app.run_server(port=8085)