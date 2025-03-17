
CREATE TABLE Idioma (
    ID_idioma INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre_idioma VARCHAR(15)
);


CREATE TABLE Voz (
    ID_voz INTEGER PRIMARY KEY AUTOINCREMENT,
    Tipo_voz VARCHAR(20)
);


CREATE TABLE Icono (
    ID_icono INTEGER PRIMARY KEY AUTOINCREMENT,
    Tipo_icono VARCHAR(20),
    Image BLOB
);


CREATE TABLE Configuracion (
    id_configuracion INTEGER PRIMARY KEY AUTOINCREMENT,
    UnidadesDistancia VARCHAR(20),
    Notificaciones BOOLEAN,
    Modo VARCHAR(20),
    Placa VARCHAR(20),
    ID_Idioma INTEGER NOT NULL,
    ID_Voz INTEGER NOT NULL,
    ID_Icono INTEGER NOT NULL,
    FOREIGN KEY (ID_Idioma) REFERENCES Idioma(ID_idioma),
    FOREIGN KEY (ID_Voz) REFERENCES Voz(ID_voz),
    FOREIGN KEY (ID_Icono) REFERENCES Icono(ID_icono)
);


CREATE TABLE Usuario (
    ID_Usuario INTEGER PRIMARY KEY AUTOINCREMENT,
    Fecha_registro DATETIME,
    Email VARCHAR(40),
    Nombre VARCHAR(30),
    ID_Config INTEGER NOT NULL,
    FOREIGN KEY (ID_Config) REFERENCES Configuracion(id_configuracion)
);


CREATE TABLE Direcciones (
    ID_Direcciones INTEGER PRIMARY KEY AUTOINCREMENT,
    Direccion VARCHAR(30)
);


CREATE TABLE Configuracion_Direcciones (
    ID_configuracion_direcciones INTEGER PRIMARY KEY AUTOINCREMENT,
    ID_direccion INTEGER NOT NULL,
    ID_configuracion INTEGER NOT NULL,
    FOREIGN KEY (ID_direccion) REFERENCES Direcciones(ID_Direcciones),
    FOREIGN KEY (ID_configuracion) REFERENCES Configuracion(id_configuracion)
);
