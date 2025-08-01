-- DROP DATABASE IF EXISTS libreria;
-- CREATE DATABASE libreria;
USE libreria;

-- tabla de categorias
CREATE TABLE categorias(
categoria_id INT NOT NULL AUTO_INCREMENT,
nombre VARCHAR(40) NOT NULL,
PRIMARY KEY (categoria_id)
)ENGINE = InnoDB; 

-- tabla de productos
CREATE TABLE productos(
producto_id INT NOT NULL AUTO_INCREMENT,
nombre VARCHAR(40) NOT NULL,
categoria_id INT NOT NULL, 
precio REAL NOT NULL,
stock INT DEFAULT 0,
PRIMARY KEY (producto_id),
FOREIGN KEY (categoria_id) REFERENCES categorias(categoria_id)
)ENGINE = InnoDB; 

-- DROP TABLE IF EXISTS clientes
-- tabla de clientes
CREATE TABLE clientes(
cliente_id INT NOT NULL AUTO_INCREMENT,
nombre VARCHAR(40) NOT NULL,
apellido VARCHAR(40) NOT NULL,
email VARCHAR(100),
fecha_registro DATE NOT NULL,
PRIMARY KEY (cliente_id)
)ENGINE = InnoDB; 


-- tabla de ventas
CREATE TABLE ventas(
venta_id INT NOT NULL AUTO_INCREMENT,
cliente_id INT NOT NULL,
fecha DATETIME DEFAULT CURRENT_TIMESTAMP,
total DECIMAL(10,2),
PRIMARY KEY (venta_id),
FOREIGN KEY (cliente_id) REFERENCES clientes(cliente_id) 
)ENGINE = InnoDB; 


-- tabla de detalle_ventas
CREATE TABLE detalle_ventas(
detalle_ventas_id INT NOT NULL AUTO_INCREMENT,
venta_id INT NOT NULL,
producto_id INT NOT NULL,
cantidad INT NOT NULL,
subtotal REAL NOT NULL,
PRIMARY KEY (detalle_ventas_id),
FOREIGN KEY (venta_id) REFERENCES ventas(venta_id),
FOREIGN KEY (producto_id) REFERENCES productos(producto_id) 
)ENGINE = InnoDB; 

-- datos de categorias
INSERT INTO categorias (nombre) VALUES
("Servicios"),
("Palería"),
("Regalería"),
("Tecnología");



-- datos de clientes
INSERT INTO clientes (nombre, apellido, email, fecha_registro) VALUES
("Ramón","Vargas","ramonv@gmail.com", "2025-02-02"),
("Elsa","D'Ambrosio","elsada@gmail.com", "2024-11-23"),
("Rayla","Vargas","ramonv@gmail.com", "2024-09-19"),
("Frieren","Hana","frierenh@gmail.com", "2023-07-23");

-- datos de productos
INSERT INTO productos (nombre, categoria_id, precio, stock) VALUES
("Lápiz HB", 2, 100, 200),
("Cuaderno A4", 2, 5500, 50),
("Taza personalizada", 3, 6700, 20),
("Pendrive 16GB", 4, 8999, 0),
('Hoja a color', 1, 500, 150),
('Cuaderno A3', 2, 7000, 30),
('Cartuchera Objetos', 3, 8710, 25),
('Pendrive 32GB', 3, 10899, 20),
('Lapicera Parker', 3, 3500, 160),
('Bolígrafo FILGO Gel Pop Glitter', 3, 9500, 50),
('Mouse Inalámbrico M280 Logitech', 4, 16890, 10);

-- Consultas
SELECT nombre, precio
FROM productos
WHERE stock > 10
ORDER BY precio DESC


