#Librerias de bases de datos
import psycopg2
import datetime

#Condiciones de la conexión a la base de datos
user = "postgres"
password = "Usuario1"
host = "localhost"
port = 5432
database = "Proyecto GestionBD"

#Fecha de registros de cambios para el registro de auditoría:
def registrarFecha():
    d=datetime.datetime.now()
    return d

#Se crea la conexión
def crear_Conexion():
    try:
        #Se pasa las condiciones a la función de conexión
        conn=psycopg2.connect(
            host=host,
            user=user,
            password=password,
            port=port,
            database=database
        )
        print(f"La base de datos {database} esta conectada.")
        return conn

    except Exception as Error:
        print("Error en la conexión.")
        return None

def conexionPrueba(conn):
    #Se crea el cursor.
    cur=conn.cursor()
    cur.execute("SELECT version();")
    row=cur.fetchone()
    print(f"Version: \n{row}")

#Funcion para crear tablas
def crearTablas(conn):
    cur=conn.cursor()
    instruccion="""CREATE TABLE IF NOT EXISTS Equipo (
        ID_Equipo SERIAL PRIMARY KEY,
        Marca VARCHAR(100),
        Modelo VARCHAR(100),
        Fecha_compra DATE
    );
    """
    cur.execute(instruccion)
    cur.commit()

#Funcion para busquedas
def buscarSalas(conn):
    cur=conn.cursor()
    cur.execute("SELECT Sala, Tipo FROM Sala")
    rows=cur.fetchall()
    for row in rows:
        print(row)
    return rows

#Función para registrar un equipo
def registrarEquipo(conn, marca, modelo, id_sala):
    cur=conn.cursor()
    instruccion="""INSERT INTO Equipo (Marca, Modelo, Fecha_compra )
    VALUES
        (%s, %s, %s, %s)
    """
    cur.execute(instruccion, {marca, modelo, fecha_compra, id_sala})
    conn.commit()

#Buscar equipos
def buscarEquipo(conn):
    cur=conn.cursor()
    instruccion="SELECT Marca, Modelo, Fecha_compra FROM Equipo"
    cur.execute(instruccion)
    rows=cur.fetchall()
    for row in rows:
        print(row)
    return rows