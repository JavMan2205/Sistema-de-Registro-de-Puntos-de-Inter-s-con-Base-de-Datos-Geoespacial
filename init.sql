CREATE EXTENSION IF NOT EXISTS postgis;

CREATE TABLE IF NOT EXISTS puntos (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    descripcion TEXT,
    categoria VARCHAR(50),
    ubicacion GEOGRAPHY(POINT, 4326)
);

INSERT INTO puntos (nombre, descripcion, categoria, ubicacion) VALUES
('Tikal Futura', 'Centro de negocios y comercial', 'Servicio', 'POINT(-90.5515 14.6225)'),
('Teatro Nacional', 'Centro Cultural Miguel Ángel Asturias', 'Cultural', 'POINT(-90.5186 14.6256)'),
('Cerrito del Carmen', 'Ermita histórica y parque', 'Natural', 'POINT(-90.5055 14.6433)'),
('Mapa en Relieve', 'Obra de ingeniería histórica', 'Cultural', 'POINT(-90.5083 14.6558)'),
('Zoológico La Aurora', 'Parque zoológico nacional', 'Natural', 'POINT(-90.5315 14.5947)');