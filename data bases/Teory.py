#Crear base de datos:
import sqlite3

conexion = sqlite3.connect("baseDatos.db")

#Crear tabla:
cursor = conexion.cursor()
cursor.execute("CREATE TABLE PERSONAS(nombre TEXT, apellido TEXT, edad INTEGRER)")
conexion.commit()

#Insertar una fila:
cursor.execute("INSERT INTO PERSONAS VALUES ('Antonio', 'Rodriguez', 20)")
conexion.commit()

#Insertar varias filas:
lista_elementos = [ ('Sergio','Fernandez',18), ('Pablo','Escanez',16) ]
cursor.executemany("INSERT INTO PERSONAS VALUES (?,?,?)", lista_elementos)
conexion.commit()

#Consultar elementos:
cursor.execute("SELECT * FROM PERSONAS")
personas = cursor.fetchall()
for i in personas:
    print(i)
print("\n")

#Consultar datos con WHERE:
cursor.execute("SELECT * FROM PERSONAS WHERE edad > 17")
seleccionadas = cursor.fetchall()
for i in seleccionadas:
    print(i)
print("\n")

#Ordenar por datos:
cursor.execute("SELECT * FROM PERSONAS ORDER BY edad")
ordenadas = cursor.fetchall()
for i in ordenadas:
    print(i)
print("\n")

#Ordenar datos:
cursor.execute("DELETE FROM PERSONAS WHERE edad = 16")
conexion.commit()

#Actualizar datos:
cursor.execute("UPDATE PERSONAS SET edad = 25 WHERE nombre = 'Antonio'")
conexion.commit()

conexion.close()