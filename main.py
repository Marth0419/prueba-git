"""Demostración del sistema escolar en capas.

Registra dos alumnos, los guarda en datos.txt, y luego los
recupera con un Sistema distinto para comprobar que el archivo
funciona. Se corre con: python main.py
"""

from sistema import Sistema

s = Sistema()
s.registrar("219876543", "Ana Ruiz")
s.registrar("219876544", "Luis Soto")
s.guardar("datos.txt")
print("Guardado. Ahora abro otro sistema y cargo el archivo:")

otro = Sistema()
otro.cargar("datos.txt")
otro.listar()
