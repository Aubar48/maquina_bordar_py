<figure><img src="/ISPC_portada.png" alt="logo" style="height: 200px;"></figure>


Proyecto: Diseño y Desarrollo de Objetos
Objetivo
El propósito de este proyecto es diseñar y desarrollar una clase en Python que represente un objeto con funcionalidad lógica, aplicando TDD (Desarrollo Guiado por Pruebas), conceptos de Programación Orientada a Objetos (POO) y diseñando la base de datos correspondiente.

Instrucciones del Proyecto
1. Selección y Diseño del Objeto
Objeto Seleccionado: [Maquina_bordar]

Este proyecto se basa en la representación de un objeto [ Este proyecto se basa en la representación de una máquina de bordar, un dispositivo automatizado que realiza bordados complejos en tela mediante la selección de diseños predefinidos y la aplicación de hilos de diversos colores. La máquina gestiona de manera eficiente la creación de patrones bordados, controlando la selección de hilos y el tiempo necesario para completar cada diseño.]. 
Los comportamientos clave definidos para este objeto son:

[Clase Hilo]: [Esta clase representa los hilos utilizados en el proceso de bordado. Su comportamiento clave incluye la gestión de la cantidad de hilo disponible y el color del hilo. La lógica de programación garantiza que se deduzca la cantidad de hilo utilizado durante cada proceso de bordado, evitando el uso de hilos agotados.].
<br>
[Clase Diseño]: [Esta clase maneja los diferentes diseños que la máquina de bordar puede ejecutar. Los comportamientos clave incluyen la definición de la complejidad del diseño y la lista de colores necesarios. La lógica de programación asegura que los diseños se seleccionen y validen de acuerdo con la disponibilidad de hilos y la complejidad deseada.].
<br>
[Clase Bordar]: [Esta clase representa el proceso de bordado en sí. Gestiona la ejecución del diseño seleccionado utilizando los hilos disponibles. La lógica de programación incluye la asignación de hilos al diseño, el cálculo del tiempo estimado para completar el bordado, y la actualización de los recursos de hilo tras la finalización del proceso.].
Además, se incluye un método estándar de definición en la clase, como __str__(self) para proporcionar una representación legible del objeto.

2. Desarrollo Guiado por Pruebas (TDD)
En este proyecto, se siguió el enfoque de TDD. Los pasos fueron los siguientes:

Escritura de pruebas unitarias: Se escribieron las pruebas que verifican la funcionalidad esperada de cada método en la clase.
Implementación de la clase: Se implementó la clase para pasar las pruebas definidas.
Refactorización: Se realizó la refactorización del código según fuera necesario para mejorar su eficiencia y claridad sin romper las pruebas existentes.
3. Diseño de Base de Datos
Para representar el objeto en una base de datos, se diseñó una estructura relacional que incluye las siguientes tablas:

<figure><img src="/maquina_bordar.jpg" alt="logo" style="height: 400px;"></figure>


Tabla diseños:

id: Identificador único del diseño (PRIMARY KEY).
nombre: Nombre del diseño.
complejidad: Nivel de complejidad del diseño.
colores: Colores involucrados en el diseño.
Tabla hilos:

id: Identificador único del hilo (PRIMARY KEY).
color: Color del hilo.
cantidad: Cantidad disponible de este color.
Tabla bordados:

id: Identificador único del bordado (PRIMARY KEY).
diseño_id: Referencia al diseño utilizado (FOREIGN KEY).
hilo_id: Referencia al hilo utilizado (FOREIGN KEY).
tiempo_estimado: Tiempo estimado para completar el bordado.
Sentencias SQL
Creación de las tablas: Se incluyen las sentencias CREATE TABLE para cada tabla con sus respectivas llaves primarias y foráneas.
Inserción de datos: Se proporcionan 10 sentencias INSERT con datos de ejemplo.
Consultas: Se desarrollaron 5 consultas SELECT para obtener información relevante de la base de datos.

4. Documentación y Reflexión en Video
Se ha creado un video de 180 segundos en el que se explica: https://youtu.be/vDCjr1OwjF4

Código fuente: Se demuestra cómo se aplican los principios de abstracción y encapsulamiento en la clase desarrollada.
Experiencia con TDD: Se describe brevemente cómo fue el proceso de desarrollo siguiendo TDD.
Programa en funcionamiento: Se muestra el programa en acción, verificando que cumple con los comportamientos definidos.

Requisitos
Python 3.8+
[Dependencias adicionales si las hay]
Cómo Ejecutar
Clonar el repositorio:

bash
Copiar código
git clone https://github.com/Aubar48/maquina_bordar_py
cd tu_repositorio
Ejecutar las pruebas unitarias:

bash
Copiar código
python -m unittest src/test_[nombre_clase].py
Cargar la base de datos:

sql
Copiar código
-- Ejecutar el archivo esquema.sql en tu gestor de base de datos
-- Luego, cargar los datos de ejemplo con datos.sql
Ejecutar el programa:

bash
Copiar código
python src/[nombre_clase].py
Reflexión Final
El desarrollo de este proyecto permitió la aplicación práctica de los conceptos de POO y TDD, además del diseño de una base de datos. La experiencia con TDD ayudó a asegurar que el código fuera robusto desde el inicio, y la implementación de la base de datos proporcionó una representación estructurada del objeto.