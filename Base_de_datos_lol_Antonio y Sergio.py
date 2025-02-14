import sqlite3

def conectar():
    return sqlite3.connect("lol.db")

def crear_tablas():
    conexion = conectar()
    cursor = conexion.cursor()
    
    cursor.execute('''CREATE TABLE IF NOT EXISTS Regiones (
                        id_region INTEGER PRIMARY KEY AUTOINCREMENT,
                        nombre_region TEXT UNIQUE NOT NULL)''')
    
    cursor.execute('''CREATE TABLE IF NOT EXISTS Lineas (
                        id_linea INTEGER PRIMARY KEY AUTOINCREMENT,
                        nombre_linea TEXT UNIQUE NOT NULL)''')
    
    cursor.execute('''CREATE TABLE IF NOT EXISTS Personajes (
                        id_personaje INTEGER PRIMARY KEY AUTOINCREMENT,
                        nombre TEXT UNIQUE NOT NULL,
                        anyo_salida INTEGER NOT NULL,
                        fuente_de_poder TEXT NOT NULL,
                        id_region INTEGER,
                        id_linea INTEGER,
                        FOREIGN KEY(id_region) REFERENCES Regiones(id_region),
                        FOREIGN KEY(id_linea) REFERENCES Lineas(id_linea))''')
    
    conexion.commit()
    conexion.close()

def insertar_personaje(nombre, anyo_salida, fuente_de_poder, id_region, id_linea):
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("INSERT INTO Personajes (nombre, anyo_salida, fuente_de_poder, id_region, id_linea) VALUES (?, ?, ?, ?, ?)",
                   (nombre, anyo_salida, fuente_de_poder, id_region, id_linea))
    conexion.commit()
    conexion.close()

def insertar_region(nombre_region):
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("INSERT INTO Regiones (nombre_region) VALUES (?)", (nombre_region,))
    conexion.commit()
    conexion.close()

def insertar_linea(nombre_linea):
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("INSERT INTO Lineas (nombre_linea) VALUES (?)", (nombre_linea,))
    conexion.commit()
    conexion.close()

def listar_personajes():
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM Personajes")
    personajes = cursor.fetchall()
    for p in personajes:
        print(p)
    conexion.close()

def listar_regiones():
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM Regiones")
    regiones = cursor.fetchall()
    for r in regiones:
        print(r)
    conexion.close()

def listar_lineas():
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM Lineas")
    lineas = cursor.fetchall()
    for l in lineas:
        print(l)
    conexion.close()

def actualizar_personaje(id_personaje, nuevo_nombre, nuevo_anyo, nueva_fuente, nueva_region, nueva_linea):
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("UPDATE Personajes SET nombre=?, anyo_salida=?, fuente_de_poder=?, id_region=?, id_linea=? WHERE id_personaje=?",
                   (nuevo_nombre, nuevo_anyo, nueva_fuente, nueva_region, nueva_linea, id_personaje))
    conexion.commit()
    conexion.close()

def actualizar_region(id_region, nuevo_nombre):
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("UPDATE Regiones SET nombre_region=? WHERE id_region=?", (nuevo_nombre, id_region))
    conexion.commit()
    conexion.close()

def actualizar_linea(id_linea, nuevo_nombre):
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("UPDATE Lineas SET nombre_linea=? WHERE id_linea=?", (nuevo_nombre, id_linea))
    conexion.commit()
    conexion.close()

def eliminar_personaje(id_personaje):
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("DELETE FROM Personajes WHERE id_personaje=?", (id_personaje,))
    conexion.commit()
    conexion.close()

def eliminar_region(id_region):
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("DELETE FROM Regiones WHERE id_region=?", (id_region,))
    conexion.commit()
    conexion.close()

def eliminar_linea(id_linea):
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("DELETE FROM Lineas WHERE id_linea=?", (id_linea,))
    conexion.commit()
    conexion.close()

def menu():
    crear_tablas()
    continuar = True
    while continuar:
        print("\nMenú:")
        print("1. Agregar Región")
        print("2. Agregar Línea")
        print("3. Agregar Personaje")
        print("4. Listar Personajes")
        print("5. Listar Regiones")
        print("6. Listar Líneas")
        print("7. Actualizar Personaje")
        print("8. Actualizar Región")
        print("9. Actualizar Línea")
        print("10. Eliminar Personaje")
        print("11. Eliminar Región")
        print("12. Eliminar Línea")
        print("13. Salir")
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            nombre = input("Nombre de la región: ")
            insertar_region(nombre)
        elif opcion == "2":
            nombre = input("Nombre de la línea: ")
            insertar_linea(nombre)
        elif opcion == "3":
            nombre = input("Nombre del personaje: ")
            anyo = int(input("Año de salida: "))
            poder = input("Fuente de poder: ")
            id_region = int(input("ID de la región: "))
            id_linea = int(input("ID de la línea: "))
            insertar_personaje(nombre, anyo, poder, id_region, id_linea)
        elif opcion == "4":
            listar_personajes()
        elif opcion == "5":
            listar_regiones()
        elif opcion == "6":
            listar_lineas()
        elif opcion == "7":
            id_p = int(input("ID del personaje a actualizar: "))
            nombre = input("Nuevo nombre: ")
            anyo = int(input("Nuevo año de salida: "))
            poder = input("Nueva fuente de poder: ")
            id_region = int(input("Nuevo ID de región: "))
            id_linea = int(input("Nuevo ID de línea: "))
            actualizar_personaje(id_p, nombre, anyo, poder, id_region, id_linea)
        elif opcion == "8":
            id_r = int(input("ID de la región a actualizar: "))
            nuevo_nombre = input("Nuevo nombre de la región: ")
            actualizar_region(id_r, nuevo_nombre)
        elif opcion == "9":
            id_l = int(input("ID de la línea a actualizar: "))
            nuevo_nombre = input("Nuevo nombre de la línea: ")
            actualizar_linea(id_l, nuevo_nombre)
        elif opcion == "10":
            id_p = int(input("ID del personaje a eliminar: "))
            eliminar_personaje(id_p)
        elif opcion == "11":
            id_r = int(input("ID de la región a eliminar: "))
            eliminar_region(id_r)
        elif opcion == "12":
            id_l = int(input("ID de la línea a eliminar: "))
            eliminar_linea(id_l)
        elif opcion == "13":
            continuar = False
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    menu()
