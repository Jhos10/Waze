INSERT INTO Usuario (Fecha_registro, Email, Nombre, ID_Config)
VALUES 
(datetime('now'), 'usuario1@example.com', 'Juan', 1),
(datetime('now'), 'usuario2@example.com', 'Jhostin', 2);

INSERT INTO Direcciones (Direccion) 
VALUES 
('Carrera 7 #45-67, Bogotá'),
('Calle 50 #10-15, Medellín'),
('Avenida 30 de Agosto #16-20, Pereira'),
('Calle 12 #34-56, Cali'),
('Carrera 15 #78-90, Barranquilla'),
('Calle 9 #27-31, Cartagena'),
('Avenida Santander #22-40, Manizales'),
('Carrera 4 #14-22, Bucaramanga'),
('Calle 19 #7-89, Cúcuta'),
('Carrera 6 #23-45, Armenia');


INSERT INTO Idioma (nombre_idioma)
VALUES 
('Español'),
('Portugues'),
('Inglés');


INSERT INTO Voz (Tipo_voz)
VALUES 
('Ferxo'),
('BadBunny'),
('Maluma');


INSERT INTO Icono (Tipo_icono, Image)
VALUES 
('Carro','.\\images\\iconos\\carro-deportivo.png'),
('Moto', '.\\images\\iconos\\moto.png');


INSERT INTO Configuracion (UnidadesDistancia, Notificaciones, Modo, Placa, ID_Idioma, ID_Voz, ID_Icono)
VALUES 
('Kilómetros', 1, 'Día', 'ABC123', 1, 1, 1), -- Configuración para Juan
('Millas', 0, 'Noche', 'XYZ789', 2, 2, 2);   -- Configuración para Jhostin

INSERT INTO Configuracion_Direcciones (ID_direccion, ID_configuracion)
VALUES 
-- Direcciones para Juan (ID_Config = 1)
(1, 1), -- Nueva dirección para Juan
(2, 1), -- Nueva dirección para Juan
(3, 1), -- Nueva dirección para Juan

-- Direcciones para Jhostin (ID_Config = 2)
(4, 2), -- Nueva direccion para Jhostin
(5, 2), -- Nueva dirección para Jhostin
(6, 2); -- Nueva dirección para Jhostin
