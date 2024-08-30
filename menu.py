import mysql.connector
from maquina_bordar import MaquinaBordar, Diseño, Hilo
# Función para conectar a la base de datos MySQL
def conectar_bd():
    conexion = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="MaquinaBordarDB"
    )
    return conexion

# Función para listar todos los diseños
def listar_diseños(conexion):
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM diseños;")
    diseños = cursor.fetchall()
    for diseño in diseños:
        print(diseño)

# Función para listar todos los hilos
def listar_hilos(conexion):
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM hilos;")
    hilos = cursor.fetchall()
    for hilo in hilos:
        print(hilo)

# Función para buscar diseño por ID
def buscar_diseño_por_id(conexion, diseño_id):
    cursor = conexion.cursor()
    cursor.execute(f"SELECT * FROM diseños WHERE id = {diseño_id};")
    diseño = cursor.fetchone()
    return diseño

# Función para buscar hilo por ID
def buscar_hilo_por_id(conexion, hilo_id):
    cursor = conexion.cursor()
    cursor.execute(f"SELECT * FROM hilos WHERE id = {hilo_id};")
    hilo = cursor.fetchone()
    return hilo

# Función para insertar un nuevo diseño
def insertar_diseño(conexion, nombre, complejidad, colores):
    cursor = conexion.cursor()
    cursor.execute(f"INSERT INTO diseños (nombre, complejidad, colores) VALUES ('{nombre}', {complejidad}, '{colores}');")
    conexion.commit()

# Función para insertar un nuevo hilo
def insertar_hilo(conexion, color, cantidad):
    cursor = conexion.cursor()
    cursor.execute(f"INSERT INTO hilos (color, cantidad) VALUES ('{color}', {cantidad});")
    conexion.commit()

# Función para obtener un diseño específico por ID (Integración con Máquina Bordar)
def obtener_diseño_por_id(conexion, diseño_id):
    cursor = conexion.cursor()
    cursor.execute(f"SELECT nombre, complejidad, colores FROM diseños WHERE id = {diseño_id};")
    resultado = cursor.fetchone()
    if resultado:
        nombre, complejidad, colores = resultado
        colores = colores.split(",")  # Convertimos la cadena de colores en una lista
        return Diseño(nombre, complejidad, colores)
    return None

# Función para obtener un hilo específico por ID (Integración con Máquina Bordar)
def obtener_hilo_por_id(conexion, hilo_id):
    cursor = conexion.cursor()
    cursor.execute(f"SELECT color, cantidad FROM hilos WHERE id = {hilo_id};")
    resultado = cursor.fetchone()
    if resultado:
        color, cantidad = resultado
        return Hilo(color, cantidad)
    return None


# Menú interactivo combinado
def menu():
    conexion = conectar_bd()
    maquina = MaquinaBordar(area_max=10, velocidad=500)
    
    while True:
        print("\nMenú de Opciones:")
        print("1. Listar todos los diseños")
        print("2. Listar todos los hilos")
        print("3. Buscar diseño por ID")
        print("4. Buscar hilo por ID")
        print("5. Insertar nuevo diseño")
        print("6. Insertar nuevo hilo")
        print("7. Cargar diseño en la máquina")
        print("8. Cargar hilo en la máquina")
        print("9. Iniciar bordado")
        print("10. Cambiar hilo")
        print("11. Calcular tiempo de bordado")
        print("12. Mostrar estado de la máquina")
        print("13. Salir")
        
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            listar_diseños(conexion)

        elif opcion == "2":
            listar_hilos(conexion)

        elif opcion == "3":
            diseño_id = int(input("Ingresa el ID del diseño: "))
            diseño = buscar_diseño_por_id(conexion, diseño_id)
            if diseño:
                print(diseño)
            else:
                print("Diseño no encontrado.")

        elif opcion == "4":
            hilo_id = int(input("Ingresa el ID del hilo: "))
            hilo = buscar_hilo_por_id(conexion, hilo_id)
            if hilo:
                print(hilo)
            else:
                print("Hilo no encontrado.")

        elif opcion == "5":
            nombre = input("Nombre del diseño: ")
            complejidad = int(input("Complejidad del diseño: "))
            colores = input("Colores del diseño (separados por coma): ")
            insertar_diseño(conexion, nombre, complejidad, colores)
            print("Diseño insertado con éxito.")

        elif opcion == "6":
            color = input("Color del hilo: ")
            cantidad = int(input("Cantidad del hilo: "))
            insertar_hilo(conexion, color, cantidad)
            print("Hilo insertado con éxito.")

        elif opcion == "7":
            diseño_id = int(input("Ingresa el ID del diseño: "))
            diseño = obtener_diseño_por_id(conexion, diseño_id)
            if diseño:
                maquina.cargar_diseño(diseño)
                print(f"Diseño {diseño.nombre} cargado en la máquina.")
            else:
                print("Diseño no encontrado.")

        elif opcion == "8":
            hilo_id = int(input("Ingresa el ID del hilo: "))
            hilo = obtener_hilo_por_id(conexion, hilo_id)
            if hilo:
                maquina.cargar_hilo(hilo)
                print(f"Hilo {hilo.color} cargado en la máquina.")
            else:
                print("Hilo no encontrado.")

        elif opcion == "9":
            if maquina.iniciar_bordado():
                print("Bordado iniciado con éxito.")
            else:
                print("No se pudo iniciar el bordado. Verifica que el diseño y el hilo sean compatibles.")

        elif opcion == "10":
            hilo_id = int(input("Ingresa el ID del nuevo hilo: "))
            nuevo_hilo = obtener_hilo_por_id(conexion, hilo_id)
            if nuevo_hilo:
                maquina.cambiar_hilo(nuevo_hilo)
                print(f"Hilo cambiado a {nuevo_hilo.color}.")
            else:
                print("Hilo no encontrado.")

        elif opcion == "11":
            if maquina.diseño_actual:
                tiempo = maquina.calcular_tiempo_bordado()
                print(f"El tiempo estimado de bordado es: {tiempo} minutos.")
            else:
                print("No hay un diseño cargado en la máquina.")

        elif opcion == "12":
            print(maquina)

        elif opcion == "13":
            print("Saliendo...")
            break
        
        else:
            print("Opción no válida. Intenta de nuevo.")

    conexion.close()

if __name__ == "__main__":
    menu()
