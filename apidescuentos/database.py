from peewee import PostgresqlDatabase
from dotenv import load_dotenv

import os 

# Load the environment variables from the .env file
load_dotenv()

# Inicializamos la variable global de la base de datos, pero no la conectamos todavía
# Configuración de la base de datos PostgreSQL
db = PostgresqlDatabase(
    os.getenv('DB_COMPRAS'),
    user=os.getenv('DB_COMPRAS_USER'),
    password=os.getenv('DB_COMPRAS_PASSWORD'),
    host=os.getenv('HOST_COMPRAS'),
    port=5432
)

dbAutodw = PostgresqlDatabase(
     os.getenv('DB_DW'),
    user= os.getenv('DB_DW_USER'),
    password= os.getenv('DB_DW_PASSWORD'),
    host= os.getenv('HOST_DW'),
    port=5432
)
<<<<<<< HEAD

# Base de datos para pruebas
dbComprasDesarrollo = PostgresqlDatabase(
    'compras',
    user='compras',
    password='compras',
    host='192.168.201.12',
    port=5432
)
=======
>>>>>>> main
