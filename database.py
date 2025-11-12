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
    cur.close()

#Funcion de conexion
def Password(conn, email):
    cur=conn.cursor()
    cur.execute("SELECT contrasena FROM usuarios WHERE email = %s", (email,))
    row=cur.fetchone()
    cur.close()
    return row


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
    conn.commit()
    cur.close()

#Funcion para busquedas
def buscarSalas(conn):
    cur=conn.cursor()
    cur.execute("SELECT Sala.Sala, Tipo FROM Sala")
    rows=cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    return rows

#Función para registrar un equipo
def registrarEquipo(conn, nombre, marca, modelo, fecha_compra, id_sala):
    cur=conn.cursor()
    instruccion="""INSERT INTO Equipo (Nombre, Marca, Modelo, Fecha_compra, id_sala)
    VALUES
        (%s, %s, %s, %s, %s)
    """
    cur.execute(instruccion, (nombre, marca, modelo, fecha_compra, id_sala))
    conn.commit()
    cur.close()

#Buscar equipos
def buscarEquipo(conn):
    cur=conn.cursor()
    instruccion="""SELECT ID_Equipo, nombre, Marca, Modelo, Fecha_compra, Estado, Equipo.id_sala, sala.sala FROM Equipo JOIN sala
    ON Equipo.id_sala=sala.id_sala
    ORDER BY ID_Equipo"""
    cur.execute(instruccion)
    rows=cur.fetchall()
    for row in rows:
        print(row)
    resultado = [
        {"id_equipo": r[0], "nombre": r[1],"marca": r[2], "modelo": r[3], "fecha_compra": r[4], "estado": r[5], "id_sala": r[6], "sala": r[7]}
        for r in rows
    ]
    cur.close()
    return resultado

#Buscar reporte (TBA)
def buscarReporte(conn, id_reporte):
    cur=conn.cursor
    instruccion="""
    SELECT id_reporte, fecha_reporte, detalle, reporte.id_equipo, equipo.nombre FROM reporte JOIN equipo
    ON reporte.id_equipo=equipo.id_equipo
    ORDER BY id_reporte
    WHERE id_reporte= %s;
    """
    cur.execute(instruccion)
    rows=cur.fetchall()
    for row in rows:
        print(row)
    resultado = [
        {"id_reporte": r[0], "fecha_reporte": r[1], "detalle": r[2], "id_equipo": r[3], "nombre": r[4]}
        for r in rows
    ]
    cur.close()
    return resultado

#Eliminar equipos
def eliminarEquipo(conn, id_equipo):
    cur = conn.cursor()
    instruccion = "DELETE FROM equipo WHERE id_equipo = %s"
    cur.execute(instruccion, (id_equipo,))
    conn.commit()
    cur.close()
