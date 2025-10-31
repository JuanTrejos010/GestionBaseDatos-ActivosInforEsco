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
    #Se creo la conexion con ina variable
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

except Exception as Error:
    print("Error")

'''
finally:
    #Se cierra la consulta
    cur.close()
    conn.close()
    print("Conexion cerrada.")
'''