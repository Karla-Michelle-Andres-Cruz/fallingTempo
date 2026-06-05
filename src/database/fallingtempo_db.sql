-- --------------------------------------------------------
-- Host:                         127.0.0.1
-- Versión del servidor:         10.4.32-MariaDB - mariadb.org binary distribution
-- SO del servidor:              Win64
-- HeidiSQL Versión:             12.13.0.7147
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;


-- Volcando estructura de base de datos para fallingtempo_db
CREATE DATABASE IF NOT EXISTS `fallingtempo_db` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci */;
USE `fallingtempo_db`;

-- Volcando estructura para tabla fallingtempo_db.bajo
CREATE TABLE IF NOT EXISTS `bajo` (
    `id_bajo` int(11) NOT NULL AUTO_INCREMENT,
    `nombre` varchar(200) NOT NULL,
    `sesion_bajo` varchar(200) NOT NULL,
    PRIMARY KEY (`id_bajo`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- Volcando datos para la tabla fallingtempo_db.bajo: ~0 rows (aproximadamente)

-- Volcando estructura para tabla fallingtempo_db.bateria
CREATE TABLE IF NOT EXISTS `bateria` (
    `id_bateria` int(11) NOT NULL AUTO_INCREMENT,
    `nombre` varchar(150) NOT NULL,
    `sesion_bateria` varchar(200) NOT NULL,
    PRIMARY KEY (`id_bateria`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- Volcando datos para la tabla fallingtempo_db.bateria: ~0 rows (aproximadamente)

-- Volcando estructura para tabla fallingtempo_db.cancion
CREATE TABLE IF NOT EXISTS `cancion` (
    `id_cancion` int(11) NOT NULL AUTO_INCREMENT,
    `nombre_cancion` varchar(150) NOT NULL,
    `artista` varchar(150) NOT NULL,
    `genero` varchar(150) NOT NULL,
    `id_bateria` int(11) NOT NULL,
    `id_guitarra` int(11) NOT NULL,
    `id_bajo` int(11) NOT NULL,
    PRIMARY KEY (`id_cancion`),
    KEY `fk_cancion_bateria` (`id_bateria`),
    KEY `fk_cancion_guitarra` (`id_guitarra`),
    KEY `fk_cancion_bajo` (`id_bajo`),
    CONSTRAINT `fk_cancion_bajo` FOREIGN KEY (`id_bajo`) REFERENCES `bajo` (`id_bajo`) ON DELETE CASCADE ON UPDATE CASCADE,
    CONSTRAINT `fk_cancion_bateria` FOREIGN KEY (`id_bateria`) REFERENCES `bateria` (`id_bateria`) ON DELETE CASCADE ON UPDATE CASCADE,
    CONSTRAINT `fk_cancion_guitarra` FOREIGN KEY (`id_guitarra`) REFERENCES `guitarra` (`id_guitarra`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- Volcando datos para la tabla fallingtempo_db.cancion: ~0 rows (aproximadamente)

-- Volcando estructura para tabla fallingtempo_db.guitarra
CREATE TABLE IF NOT EXISTS `guitarra` (
    `id_guitarra` int(11) NOT NULL AUTO_INCREMENT,
    `nombre` varchar(150) NOT NULL,
    `sesion_guitarra` varchar(200) NOT NULL,
    PRIMARY KEY (`id_guitarra`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- Volcando datos para la tabla fallingtempo_db.guitarra: ~0 rows (aproximadamente)

-- Volcando estructura para tabla fallingtempo_db.recuperacion_password
CREATE TABLE IF NOT EXISTS `recuperacion_password` (
    `id` int(11) NOT NULL AUTO_INCREMENT,
    `email` varchar(100) NOT NULL,
    `codigo` varchar(10) NOT NULL,
    `fecha` timestamp NOT NULL DEFAULT current_timestamp(),
    PRIMARY KEY (`id`),
    KEY `fk_recuperacion_usuario` (`email`),
    CONSTRAINT `fk_recuperacion_usuario` FOREIGN KEY (`email`) REFERENCES `usuarios` (`email`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- Volcando datos para la tabla fallingtempo_db.recuperacion_password: ~0 rows (aproximadamente)

-- Volcando estructura para tabla fallingtempo_db.usuarios
CREATE TABLE IF NOT EXISTS `usuarios` (
    `id_usuarios` int(11) NOT NULL AUTO_INCREMENT,
    `nombre` varchar(100) NOT NULL,
    `apellido` varchar(100) NOT NULL,
    `email` varchar(100) NOT NULL,
    `password` varchar(255) NOT NULL,
    `telefono` varchar(20) DEFAULT NULL,
    `fecha_registro` timestamp NOT NULL DEFAULT current_timestamp(),
    PRIMARY KEY (`id_usuarios`),
    UNIQUE KEY `email` (`email`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- Volcando datos para la tabla fallingtempo_db.usuarios: ~0 rows (aproximadamente)

/*!40103 SET TIME_ZONE=IFNULL(@OLD_TIME_ZONE, 'system') */;
/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;