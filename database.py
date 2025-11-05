#Librerias de bases de datos
import psycopg2

#Condiciones de la conexión a la base de datos
user = "postgres"
password = "Usuario1"
host = "localhost"
port = 5432
database = "Proyecto GestionBD"


#Se crea la conexión
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

    #Se crea el cursor.
    cur=conn.cursor()
    cur.execute("SELECT version();")
    row=cur.fetchone()
    print(f"Version: \n{row}")

except Exception as Error:
    print("Error en la conexión.")

'''
Este finally esta oculto mientras se prueba cómo está la conexión a la base de datos
finally:
    #Se cierra la consulta
    cur.close()
    conn.close()
    print("Conexion cerrada.")
'''