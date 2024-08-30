-- Crear la base de datos
CREATE DATABASE MaquinaBordarDB;

-- Usar la base de datos creada
USE MaquinaBordarDB;

-- Crear la tabla 'diseños'
CREATE TABLE diseños (
    id INTEGER PRIMARY KEY AUTO_INCREMENT, -- Identificador único para cada diseño
    nombre TEXT NOT NULL, -- Nombre del diseño
    complejidad INTEGER NOT NULL, -- Nivel de complejidad del diseño
    colores TEXT NOT NULL -- Colores utilizados en el diseño
);

-- Crear la tabla 'hilos'
CREATE TABLE hilos (
    id INTEGER PRIMARY KEY AUTO_INCREMENT, -- Identificador único para cada hilo
    color TEXT NOT NULL, -- Color del hilo
    cantidad INTEGER NOT NULL -- Cantidad disponible del hilo
);

-- Crear la tabla 'bordados'
CREATE TABLE bordados (
    id INTEGER PRIMARY KEY AUTO_INCREMENT, -- Identificador único para cada bordado
    diseño_id INTEGER, -- Referencia al diseño utilizado en el bordado
    hilo_id INTEGER, -- Referencia al hilo utilizado en el bordado
    tiempo_estimado INTEGER, -- Tiempo estimado para completar el bordado
    FOREIGN KEY (diseño_id) REFERENCES diseños(id), -- Llave foránea a la tabla 'diseños'
    FOREIGN KEY (hilo_id) REFERENCES hilos(id) -- Llave foránea a la tabla 'hilos'
);

-- Insertar datos en la tabla 'diseños'
INSERT INTO diseños (nombre, complejidad, colores) VALUES ('Flor', 2, 'rojo,azul');
INSERT INTO diseños (nombre, complejidad, colores) VALUES ('Mariposa', 3, 'amarillo,negro');
INSERT INTO diseños (nombre, complejidad, colores) VALUES ('Estrella', 1, 'amarillo,blanco');
INSERT INTO diseños (nombre, complejidad, colores) VALUES ('Corazón', 2, 'rojo,rosa');
INSERT INTO diseños (nombre, complejidad, colores) VALUES ('Sol', 3, 'amarillo,naranja');
INSERT INTO diseños (nombre, complejidad, colores) VALUES ('Luna', 2, 'blanco,gris');
INSERT INTO diseños (nombre, complejidad, colores) VALUES ('Arbol', 4, 'verde,marrón');
INSERT INTO diseños (nombre, complejidad, colores) VALUES ('Montaña', 3, 'gris,verde');
INSERT INTO diseños (nombre, complejidad, colores) VALUES ('Casa', 2, 'rojo,blanco');
INSERT INTO diseños (nombre, complejidad, colores) VALUES ('Carro', 3, 'negro,rojo');

-- Insertar datos en la tabla 'hilos'
INSERT INTO hilos (color, cantidad) VALUES ('rojo', 100);
INSERT INTO hilos (color, cantidad) VALUES ('azul', 100);
INSERT INTO hilos (color, cantidad) VALUES ('amarillo', 80);
INSERT INTO hilos (color, cantidad) VALUES ('blanco', 120);
INSERT INTO hilos (color, cantidad) VALUES ('rosa', 90);
INSERT INTO hilos (color, cantidad) VALUES ('naranja', 70);
INSERT INTO hilos (color, cantidad) VALUES ('gris', 100);
INSERT INTO hilos (color, cantidad) VALUES ('verde', 150);
INSERT INTO hilos (color, cantidad) VALUES ('marrón', 60);
INSERT INTO hilos (color, cantidad) VALUES ('negro', 110);

-- Insertar datos en la tabla 'bordados'
INSERT INTO bordados (diseño_id, hilo_id, tiempo_estimado) VALUES (1, 1, 4);
INSERT INTO bordados (diseño_id, hilo_id, tiempo_estimado) VALUES (2, 2, 6);
INSERT INTO bordados (diseño_id, hilo_id, tiempo_estimado) VALUES (3, 3, 2);
INSERT INTO bordados (diseño_id, hilo_id, tiempo_estimado) VALUES (4, 4, 4);
INSERT INTO bordados (diseño_id, hilo_id, tiempo_estimado) VALUES (5, 5, 6);
INSERT INTO bordados (diseño_id, hilo_id, tiempo_estimado) VALUES (6, 6, 5);
INSERT INTO bordados (diseño_id, hilo_id, tiempo_estimado) VALUES (7, 7, 7);
INSERT INTO bordados (diseño_id, hilo_id, tiempo_estimado) VALUES (8, 8, 3);
INSERT INTO bordados (diseño_id, hilo_id, tiempo_estimado) VALUES (9, 1, 6);
INSERT INTO bordados (diseño_id, hilo_id, tiempo_estimado) VALUES (10, 2, 4);

-- Consultas

-- Seleccionar todos los diseños con una complejidad mayor a 2
SELECT * FROM diseños WHERE complejidad > 2;

-- Seleccionar todos los hilos cuya cantidad sea menor a 50
SELECT * FROM hilos WHERE cantidad < 50;

-- Seleccionar los nombres de los diseños y los colores de hilos utilizados en cada bordado
SELECT diseños.nombre, hilos.color 
FROM bordados
JOIN diseños ON bordados.diseño_id = diseños.id
JOIN hilos ON bordados.hilo_id = hilos.id;

-- Contar cuántos bordados tienen un tiempo estimado mayor a 5
SELECT COUNT(*) FROM bordados WHERE tiempo_estimado > 5;

-- Seleccionar todos los bordados que usan el diseño con id 1
SELECT * FROM bordados WHERE diseño_id = 1;

-- Seleccionar todos los diseños que usan el color 'rojo'
SELECT * FROM diseños WHERE colores LIKE '%rojo%';

-- Seleccionar los colores y cantidades de hilos utilizados en bordados con un diseño de complejidad 3
SELECT hilos.color, hilos.cantidad 
FROM bordados 
JOIN diseños ON bordados.diseño_id = diseños.id 
JOIN hilos ON bordados.hilo_id = hilos.id 
WHERE diseños.complejidad = 3;

-- Calcular el total de hilos usados en todos los bordados
SELECT SUM(hilos.cantidad) AS total_hilos_usados 
FROM bordados 
JOIN hilos ON bordados.hilo_id = hilos.id;

-- Seleccionar los bordados ordenados por la complejidad de sus diseños de mayor a menor
SELECT bordados.id, diseños.nombre, diseños.complejidad 
FROM bordados 
JOIN diseños ON bordados.diseño_id = diseños.id 
ORDER BY diseños.complejidad DESC;

-- Contar la cantidad de bordados realizados por cada diseño
SELECT diseños.nombre, COUNT(bordados.id) AS cantidad_bordados 
FROM bordados 
JOIN diseños ON bordados.diseño_id = diseños.id 
GROUP BY diseños.nombre;

-- Calcular el tiempo promedio estimado de todos los bordados
SELECT AVG(tiempo_estimado) AS tiempo_promedio_bordado 
FROM bordados;

-- Seleccionar los nombres de los diseños y los colores y cantidades de los hilos de color 'azul'
SELECT diseños.nombre, hilos.color, hilos.cantidad 
FROM bordados 
JOIN diseños ON bordados.diseño_id = diseños.id 
JOIN hilos ON bordados.hilo_id = hilos.id 
WHERE hilos.color = 'azul';

-- Seleccionar los bordados que utilizan el diseño 'Flor' y el hilo de color 'rojo'
SELECT bordados.id, diseños.nombre, hilos.color 
FROM bordados 
JOIN diseños ON bordados.diseño_id = diseños.id 
JOIN hilos ON bordados.hilo_id = hilos.id 
WHERE diseños.nombre = 'Flor' AND hilos.color = 'rojo';
