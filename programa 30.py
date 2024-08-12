import mysql.connector

# Datos de conexión a la base de datos
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="controlescolar"
)

mycursor = mydb.cursor()
# Consulta SQL para obtener los datos de los estudiantes}


# Ejemplo de consulta SELECT
mycursor.execute("SELECT * FROM alumnos")
myresult = mycursor.fetchall()

for x in myresult:
  print(x)

# Ejemplo de consulta INSERT
sql = "INSERT INTO alumnos (nombre, direccion) VALUES (%s, %s)"
val = ("Alan Alvarado", "Cerca del 110")
mycursor.execute(sql, val)


# Ejemplo de consulta UPDATE
sql = "UPDATE alumnos SET direccion = %s WHERE nombre = %s"
val = ("Ivan Saucedo", "Por Primo")
mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "record(s) updated")

# Ejemplo de consulta DELETE
sql = "DELETE FROM alumnos WHERE nombre = %s"
val = ("Alan ALvarado",) 
mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "record(s) deleted")

mydb.close()