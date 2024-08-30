class Hilo:
    def __init__(self, color, cantidad):
        self.color = color
        self.cantidad = cantidad

class Diseño:
    def __init__(self, nombre, complejidad, colores):
        self.nombre = nombre
        self.complejidad = complejidad
        self.colores = colores

class MaquinaBordar:
    def __init__(self, area_max, velocidad):
        self.area_max = area_max
        self.velocidad = velocidad
        self.diseño_actual = None
        self.hilo_actual = None

    def cargar_diseño(self, diseño):
        self.diseño_actual = diseño

    def cargar_hilo(self, hilo):
        self.hilo_actual = hilo

    def iniciar_bordado(self):
        if not self.diseño_actual or not self.hilo_actual:
            return False
        if self.hilo_actual.color not in self.diseño_actual.colores:
            return False
        return True

    def cambiar_hilo(self, nuevo_hilo):
        self.hilo_actual = nuevo_hilo
        return True

    def calcular_tiempo_bordado(self):
        return self.diseño_actual.complejidad * 2

    def __str__(self):
        return f"Máquina de Bordar con diseño {self.diseño_actual.nombre} y hilo {self.hilo_actual.color}"

