"""Guarda y recupera alumnos en un archivo de texto."""

from modelo import Alumno


def guardar(alumnos, ruta):
    """Escribe la lista de alumnos en el archivo indicado."""
    archivo = open(ruta, "w", encoding="utf-8")
    for alumno in alumnos:
        archivo.write(alumno.codigo + ";" + alumno.nombre + "\n")
    archivo.close()


def cargar(ruta):
    """Lee el archivo indicado y retorna la lista de alumnos."""
    alumnos = []
    archivo = open(ruta, "r", encoding="utf-8")
    for linea in archivo:
        partes = linea.strip().split(";")
        alumnos.append(Alumno(partes[0], partes[1]))
    archivo.close()
    return alumnos