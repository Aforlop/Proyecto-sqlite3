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

def actualizar_personaje(id_personaje, nuevo_nombre, nuevo_anyo, nueva_fuente, nueva_region, nueva_linea):
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("UPDATE Personajes SET nombre=?, anyo_salida=?, fuente_de_poder=?, id_region=?, id_linea=? WHERE id_personaje=?",
                   (nuevo_nombre, nuevo_anyo, nueva_fuente, nueva_region, nueva_linea, id_personaje))
    conexion.commit()
    conexion.close()

def eliminar_personaje(id_personaje):
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("DELETE FROM Personajes WHERE id_personaje=?", (id_personaje,))
    conexion.commit()
    conexion.close()

