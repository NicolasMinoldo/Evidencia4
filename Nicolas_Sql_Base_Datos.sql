CREATE TABLE fabricantes (
    fabricante_id INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(50) NOT NULL,
    pais VARCHAR(50) NOT NULL
);

CREATE TABLE maquinas_fabricacion_aditiva (
    id INT PRIMARY KEY AUTO_INCREMENT,
    modelo VARCHAR(50) NOT NULL,
    estado VARCHAR(20) NOT NULL,
    material_disponible INT NOT NULL,
    nivel_calibracion INT NOT NULL,
    material_necesario INT NOT NULL,
    material_faltante VARCHAR(10) CHECK (material_faltante IN ('Si', 'No')) NOT NULL,
    fabricante_id INT,
    FOREIGN KEY (fabricante_id) REFERENCES fabricantes(fabricante_id)
);

INSERT INTO fabricantes (nombre, pais)
VALUES 
('Fabricante A', 'España'),
('Fabricante B', 'Estados Unidos'),
('Fabricante C', 'Alemania');

INSERT INTO maquinas_fabricacion_aditiva (modelo, estado, material_disponible, nivel_calibracion, material_necesario, material_faltante, fabricante_id)
VALUES 
('Cannon A1', 'en espera', 150, 5, 100, 'No', 1),
('Cannon B2', 'en proceso', 120, 8, 110, 'No', 1),
('Cannon C3', 'pausado', 80, 4, 90, 'Si', 2),
('Cannon D4', 'en espera', 50, 7, 70, 'Si', 2),
('Cannon E5', 'en proceso', 200, 6, 150, 'No', 3),
('Cannon F6', 'pausado', 180, 3, 130, 'Si', 3),
('Cannon G7', 'en espera', 110, 9, 100, 'No', 1),
('Cannon H8', 'en proceso', 90, 10, 120, 'Si', 2),
('Cannon I9', 'pausado', 60, 2, 60, 'No', 1),
('Cannon J10', 'en espera', 130, 5, 140, 'Si', 3);

SELECT * FROM maquinas_fabricacion_aditiva;

SELECT modelo FROM maquinas_fabricacion_aditiva;

SELECT * FROM maquinas_fabricacion_aditiva WHERE estado = 'pausado';

SELECT modelo, nivel_calibracion FROM maquinas_fabricacion_aditiva WHERE nivel_calibracion > 7;

SELECT * FROM maquinas_fabricacion_aditiva WHERE material_disponible < 100;