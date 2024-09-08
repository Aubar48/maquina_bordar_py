import pytest
from maquina_bordar import MaquinaBordar, Diseño, Hilo

# Fixture para inicializar los objetos necesarios para las pruebas
@pytest.fixture
def maquina_bordar_setup():
    hilo_rojo = Hilo(color="rojo", cantidad=100)
    hilo_azul = Hilo(color="azul", cantidad=100)
    diseño_simple = Diseño(nombre="Flor", complejidad=2, colores=["rojo", "azul"])
    maquina = MaquinaBordar(area_max=10, velocidad=500)
    return hilo_rojo, hilo_azul, diseño_simple, maquina

# Prueba para iniciar el bordado
def test_iniciar_bordado(maquina_bordar_setup):
    hilo_rojo, _, diseño_simple, maquina = maquina_bordar_setup
    maquina.cargar_diseño(diseño_simple)
    maquina.cargar_hilo(hilo_rojo)
    resultado = maquina.iniciar_bordado()
    assert resultado is True

# Prueba para iniciar el bordado sin diseño
def test_iniciar_bordado_sin_diseño(maquina_bordar_setup):
    _, hilo_rojo, _, maquina = maquina_bordar_setup
    maquina.cargar_hilo(hilo_rojo)
    resultado = maquina.iniciar_bordado()
    assert resultado is False

# Prueba para iniciar el bordado sin hilo
def test_iniciar_bordado_sin_hilo(maquina_bordar_setup):
    _, _, diseño_simple, maquina = maquina_bordar_setup
    maquina.cargar_diseño(diseño_simple)
    resultado = maquina.iniciar_bordado()
    assert resultado is False

# Prueba para cambiar el hilo
def test_cambiar_hilo(maquina_bordar_setup):
    _, hilo_azul, _, maquina = maquina_bordar_setup
    hilo_rojo, _, _, _ = maquina_bordar_setup
    maquina.cargar_hilo(hilo_rojo)
    maquina.cambiar_hilo(hilo_azul)
    assert maquina.hilo_actual.color == "azul"

# Prueba para calcular el tiempo de bordado
def test_calcular_tiempo_bordado(maquina_bordar_setup):
    _, _, diseño_simple, maquina = maquina_bordar_setup
    maquina.cargar_diseño(diseño_simple)
    tiempo_estimado = maquina.calcular_tiempo_bordado()
    assert tiempo_estimado == 4  # Ejemplo: 2 unidades de complejidad * 2 minutos por unidad

# Prueba para la representación de la máquina como string
def test_str(maquina_bordar_setup):
    hilo_rojo, _, diseño_simple, maquina = maquina_bordar_setup
    maquina.cargar_diseño(diseño_simple)
    maquina.cargar_hilo(hilo_rojo)
    assert str(maquina) == "Máquina de Bordar con diseño Flor y hilo rojo"

