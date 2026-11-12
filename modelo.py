"""Define las clases con los datos que maneja el sistema."""


class Alumno:
    """Representa a un alumno inscrito en el sistema."""

    def __init__(self, codigo, nombre):
        self.codigo = codigo
        self.nombre = nombre

    def describir(self):
        """Retorna el alumno en una línea, listo para imprimir."""
        return self.codigo + " " + self.nombre
    
    # cambio desde A otra vez
    