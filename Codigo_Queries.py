import psycopg2

dbname = "Icfes"
user = "taylor"
password = "1234"
host = "localhost"

conn = psycopg2.connect(dbname = dbname, user = user, password = password, host = host)

query = conn.cursor();
query.execute("select * from departamento;")
row = query.fetchone()
print(row)
print("------------------")

query = conn.cursor();
query.execute("select * from municipio;")
row = query.fetchone()
print(row)
print("------------------")

query = conn.cursor();
query.execute("select * from institucion where id_mun_pres = '70001' ;")
row = query.fetchone()
print(row)
print("------------------")

query = conn.cursor();
query.execute("select * from estudiante where id_mun_res = '70001';")
row = query.fetchone()
print(row)
print("------------------")

query = conn.cursor();
query.execute("select * from estudia where nombre = 'DISEÑO';")
row = query.fetchone()
print(row)
print("------------------")

query = conn.cursor();
query.execute("select * from familia where estrato = 'Estrato 6';")
row = query.fetchone()
print(row)
print("------------------")

query = conn.cursor();
query.execute("select * from prueba where desem_ingles = 'B2';")
row = query.fetchone()
print(row)
print("------------------")

conn.close()