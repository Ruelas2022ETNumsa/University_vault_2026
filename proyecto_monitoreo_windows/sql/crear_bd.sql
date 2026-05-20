-- ============================================================
--  crear_bd.sql
--  Crea la base de datos y tabla para el sistema de monitoreo
--  ETN921 - Teoria de Sistemas Operativos
--  Compatible con MySQL 8.0.46 (Windows)
-- ============================================================

-- Crear base de datos si no existe
CREATE DATABASE IF NOT EXISTS monitoreo_red
    CHARACTER SET utf8mb4
    COLLATE utf8mb4_unicode_ci;

USE monitoreo_red;

-- Tabla principal de muestras
CREATE TABLE IF NOT EXISTS muestras (
    id        INT AUTO_INCREMENT PRIMARY KEY,
    enlace    VARCHAR(100)   NOT NULL COMMENT 'Dominio monitoreado (ej: www.google.com)',
    fecha     DATE           NOT NULL COMMENT 'Fecha de la muestra',
    hora      TIME           NOT NULL COMMENT 'Hora de la muestra',
    rtt_max   FLOAT          NOT NULL COMMENT 'RTT maximo en ms (-1 si no responde)',
    creado_en TIMESTAMP DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB;

-- Indice para acelerar consultas por enlace y fecha
ALTER TABLE muestras ADD INDEX idx_enlace_fecha (enlace, fecha);

-- ── Scripts adicionales de utilidad ─────────────────────────

-- Ver todas las muestras
-- SELECT * FROM muestras ORDER BY fecha DESC, hora DESC;

-- Ver muestras de un enlace en particular
-- SELECT * FROM muestras WHERE enlace='www.google.com' ORDER BY fecha, hora;

-- Ver promedio de RTT por enlace
-- SELECT enlace, AVG(rtt_max) AS promedio, MAX(rtt_max) AS maximo
--   FROM muestras GROUP BY enlace;

-- Vaciar la tabla (para pruebas)
-- TRUNCATE TABLE muestras;

-- Eliminar la base de datos completa
-- DROP DATABASE monitoreo_red;

SELECT 'Base de datos monitoreo_red creada correctamente.' AS resultado;
