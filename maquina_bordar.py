class Hilo:
    def __init__(self, color, cantidad):
        self.__color = color
        self.__cantidad = cantidad

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, valor):
        if not valor or not isinstance(valor, str):
            raise ValueError("El color debe ser una cadena no vacía.")
        self.__color = valor

    @property
    def cantidad(self):
        return self.__cantidad

    @cantidad.setter
    def cantidad(self, valor):
        if not isinstance(valor, int) or valor < 0:
            raise ValueError("La cantidad debe ser un número entero no negativo.")
        self.__cantidad = valor


class Diseño:
    def __init__(self, nombre, complejidad, colores):
        self.__nombre = nombre
        self.__complejidad = complejidad
        self.__colores = colores

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, valor):
        if not valor or not isinstance(valor, str):
            raise ValueError("El nombre del diseño debe ser una cadena no vacía.")
        self.__nombre = valor

    @property
    def complejidad(self):
        return self.__complejidad

    @complejidad.setter
    def complejidad(self, valor):
        if not isinstance(valor, int) or valor < 0:
            raise ValueError("La complejidad debe ser un número entero no negativo.")
        self.__complejidad = valor

    @property
    def colores(self):
        return self.__colores

    @colores.setter
    def colores(self, valor):
        if not isinstance(valor, list) or not all(isinstance(c, str) for c in valor):
            raise ValueError("Los colores deben ser una lista de cadenas.")
        self.__colores = valor


class MaquinaBordar:
    def __init__(self, area_max, velocidad):
        self.__area_max = area_max
        self.__velocidad = velocidad
        self.__diseño_actual = None
        self.__hilo_actual = None

    @property
    def area_max(self):
        return self.__area_max

    @area_max.setter
    def area_max(self, valor):
        if not isinstance(valor, int) or valor <= 0:
            raise ValueError("El área máxima debe ser un número entero positivo.")
        self.__area_max = valor

    @property
    def velocidad(self):
        return self.__velocidad

    @velocidad.setter
    def velocidad(self, valor):
        if not isinstance(valor, int) or valor <= 0:
            raise ValueError("La velocidad debe ser un número entero positivo.")
        self.__velocidad = valor

    @property
    def diseño_actual(self):
        return self.__diseño_actual

    @diseño_actual.setter
    def diseño_actual(self, diseño):
        if not isinstance(diseño, Diseño):
            raise ValueError("El diseño actual debe ser una instancia de la clase Diseño.")
        self.__diseño_actual = diseño

    @property
    def hilo_actual(self):
        return self.__hilo_actual

    @hilo_actual.setter
    def hilo_actual(self, hilo):
        if not isinstance(hilo, Hilo):
            raise ValueError("El hilo actual debe ser una instancia de la clase Hilo.")
        self.__hilo_actual = hilo

    def cargar_diseño(self, diseño):
        self.diseño_actual = diseño

    def cargar_hilo(self, hilo):
        self.hilo_actual = hilo

    def iniciar_bordado(self):
        if not self.__diseño_actual or not self.__hilo_actual:
            return False
        if self.__hilo_actual.color not in self.__diseño_actual.colores:
            return False
        return True

    def cambiar_hilo(self, nuevo_hilo):
        if not isinstance(nuevo_hilo, Hilo):
            raise ValueError("El nuevo hilo debe ser una instancia de la clase Hilo.")
        self.__hilo_actual = nuevo_hilo
        return True

    def calcular_tiempo_bordado(self):
        if not self.__diseño_actual:
            raise ValueError("No hay diseño cargado para calcular el tiempo de bordado.")
        return self.__diseño_actual.complejidad * 2

    def __str__(self):
        diseño_nombre = self.__diseño_actual.nombre if self.__diseño_actual else "Ninguno"
        hilo_color = self.__hilo_actual.color if self.__hilo_actual else "Ninguno"
        return f"Máquina de Bordar con diseño {diseño_nombre} y hilo {hilo_color}"
