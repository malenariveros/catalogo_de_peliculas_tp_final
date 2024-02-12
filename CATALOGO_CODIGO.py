# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal.
"""
import os 

class Catalogo:
    def __init__(self, nombre_archivo):
        self.peliculas = {"accion": [], "comedia": [], "drama": [], "terror": [], "documentales": [], "ciencia ficcion": []}
        self.nombre_archivo = nombre_archivo
        self.__confirmar_genero = "accion", "comedia", "drama", "terror", "documentales", "ciencia ficcion"

    def mostrar_menu(self):
        print("Menú:")
        print("1. Agregar Película")
        print("2. Listar Películas")
        print("3. Eliminar catálogo películas")
        print("4. Salir")

    def ejecutar_opcion(self, opcion):
        if opcion == 1:
            self.agregar_pelicula()
        elif opcion == 2:
            self.listar_peliculas()
        elif opcion == 3:
            self.eliminar_catalogo()
        elif opcion == 4:
            self.salir()
        else:
            print("Opción no válida. Por favor, selecciona una opción del menú.")

    def agregar_pelicula(self):
        genero = input("Ingrese el género de la película (Accion, Comedia, Drama, Terror, Documentales, Ciencia ficcion): ").lower()
        while genero not in self.__confirmar_genero:
            print("Ingrese una opción válida.")
            genero = input("Ingrese el género de la película (Accion, Comedia, Drama, Terror, Documentales, Ciencia ficcion): ").lower()
        titulo = input("Ingrese el título de la película: ")
        duracion = input("Ingrese la duración de la película en minutos: ")
        director = input("Ingrese el nombre del director de la película: ")

        nueva_pelicula = (titulo, duracion, director)
        self.peliculas[genero].append(nueva_pelicula)

        with open("C:/Ada/tp_catalogo_peliculas.py//" + self.nombre_archivo, 'w') as archivo:
            for genero, peliculas in self.peliculas.items():
                archivo.write(f'{genero}:\n')
                
                for pelicula in peliculas:
                    archivo.write(f'\t{pelicula[0]}, {pelicula[1]} minutos, dirigida por {pelicula[2]}\n')

    def listar_peliculas(self):
        if os.path.exists("C:/Ada/tp_catalogo_peliculas.py//" + self.nombre_archivo):
            with open("C:/Ada/tp_catalogo_peliculas.py//" + self.nombre_archivo, mode="r") as archivo:
                contenido = archivo.read()
                print(contenido)
        else:
            print("Películas inexistentes.")

    def eliminar_catalogo(self):
        if os.path.exists("C:/Ada/tp_catalogo_peliculas.py//" + self.nombre_archivo):
            os.remove("C:/Ada/tp_catalogo_peliculas.py//" + self.nombre_archivo)
            print("El archivo ha sido eliminado.")
        else:
            print("El archivo no existe.")

    def salir(self):
        print("Salida exitosa.")

nombre_catalogo = input("Ingrese un nombre para el catálogo: ")
catalogo = Catalogo(nombre_catalogo)

while True:
    catalogo.mostrar_menu()
    opcion = int(input("Seleccione una opción: "))

    if opcion == 4:
        break

    catalogo.ejecutar_opcion(opcion)
