-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 14-05-2026 a las 20:24:14
-- Versión del servidor: 10.4.28-MariaDB
-- Versión de PHP: 8.0.28

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `fallingtempo_db`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `bajo`
--

CREATE TABLE `bajo` (
  `id_bajo` int(11) NOT NULL,
  `nombre` varchar(200) NOT NULL,
  `sesion_bajo` varchar(200) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `bateria`
--

CREATE TABLE `bateria` (
  `id_bateria` int(11) NOT NULL,
  `nombre` varchar(150) NOT NULL,
  `sesion_bateria` varchar(200) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `cancion`
--

CREATE TABLE `cancion` (
  `id_cancion` int(11) NOT NULL,
  `nombre_cancion` varchar(150) NOT NULL,
  `artista` varchar(150) NOT NULL,
  `genero` varchar(150) NOT NULL,
  `id_bateria` int(11) NOT NULL,
  `id_guitarra` int(11) NOT NULL,
  `id_bajo` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `favorito_user`
--

CREATE TABLE `favorito_user` (
  `id_favorito` int(11) NOT NULL,
  `id_cancion` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `recuperacion_password`
--

CREATE TABLE `recuperacion_password` (
    `id` INT AUTO_INCREMENT PRIMARY KEY,
    `email` VARCHAR(100),
    `codigo` VARCHAR(10),
    `expiracion` DATETIME
);

--
-- Estructura de tabla para la tabla `guitarra`
--

CREATE TABLE `guitarra` (
  `id_guitarra` int(11) NOT NULL,
  `nombre` varchar(150) NOT NULL,
  `sesion_guitarra` varchar(200) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `usuarios`
--

CREATE TABLE `usuarios` (
  `id_usuarios` int(11) NOT NULL,
  `nombre` varchar(100) NOT NULL,
  `email` varchar(100) NOT NULL,
  `password` varchar(100) NOT NULL,
  `fecha_registro` timestamp NOT NULL DEFAULT current_timestamp(),
  `apellido` varchar(100) NOT NULL,
  `telefono` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `bajo`
--
ALTER TABLE `bajo`
  ADD PRIMARY KEY (`id_bajo`);

--
-- Indices de la tabla `bateria`
--
ALTER TABLE `bateria`
  ADD PRIMARY KEY (`id_bateria`);

--
-- Indices de la tabla `cancion`
--
ALTER TABLE `cancion`
  ADD PRIMARY KEY (`id_cancion`),
  ADD KEY `id_bateria` (`id_bateria`),
  ADD KEY `id_guitarra` (`id_guitarra`),
  ADD KEY `id_bajo` (`id_bajo`);

--
-- Indices de la tabla `favorito_user`
--
ALTER TABLE `favorito_user`
  ADD KEY `id_cancion` (`id_cancion`);

--
-- Indices de la tabla `guitarra`
--
ALTER TABLE `guitarra`
  ADD PRIMARY KEY (`id_guitarra`);

--
-- Indices de la tabla `usuarios`
--
ALTER TABLE `usuarios`
  ADD PRIMARY KEY (`id_usuarios`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `bajo`
--
ALTER TABLE `bajo`
  MODIFY `id_bajo` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `bateria`
--
ALTER TABLE `bateria`
  MODIFY `id_bateria` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `cancion`
--
ALTER TABLE `cancion`
  MODIFY `id_cancion` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `guitarra`
--
ALTER TABLE `guitarra`
  MODIFY `id_guitarra` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `usuarios`
--
ALTER TABLE `usuarios`
  MODIFY `id_usuarios` int(11) NOT NULL AUTO_INCREMENT;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `cancion`
--
ALTER TABLE `cancion`
  ADD CONSTRAINT `id_bajo` FOREIGN KEY (`id_bajo`) REFERENCES `bajo` (`id_bajo`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `id_bateria` FOREIGN KEY (`id_bateria`) REFERENCES `bateria` (`id_bateria`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `id_guitarra` FOREIGN KEY (`id_guitarra`) REFERENCES `guitarra` (`id_guitarra`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Filtros para la tabla `favorito_user`
--
ALTER TABLE `favorito_user`
  ADD CONSTRAINT `id_cancion` FOREIGN KEY (`id_cancion`) REFERENCES `cancion` (`id_cancion`) ON DELETE CASCADE ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
