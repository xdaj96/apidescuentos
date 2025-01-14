from peewee import PostgresqlDatabase
 
# Inicializamos la variable global de la base de datos, pero no la conectamos todavía
# Configuración de la base de datos PostgreSQL
db = PostgresqlDatabase(
    'compras',
    user='compras',
    password='compras',
    host='localhost',
    port=5432
)

dbAutodw = PostgresqlDatabase(
    'autofarmadw',
    user='autofarmadw',
    password='autofarmadw',
    host='192.168.201.12',
    port=5432
)

