"""Contiene la lógica del sistema escolar."""

from modelo import Alumno
import almacen


class Sistema:
    """Administra los alumnos registrados y su almacenamiento."""
    
    def __init__(self):
        self._alumnos = []

    def registrar(self, codigo, nombre):
        """Da de alta un alumno nuevo."""
        self._alumnos.append(Alumno(codigo, nombre))

    def listar(self):
        """Imprime en pantalla todos los alumnos registrados."""
        for alumno in self._alumnos:
            print(alumno.describir())

    def guardar(self, ruta):
        """Pide al almacén que escriba los alumnos en el archivo."""
        almacen.guardar(self._alumnos, ruta)

    def cargar(self, ruta):
        """Reemplaza los alumnos con los que haya en el archivo."""
        self._alumnos = almacen.cargar(ruta)


        
