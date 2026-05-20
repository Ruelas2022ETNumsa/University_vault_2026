-- ============================================================
--  fix_auth_php71.sql
--
--  ATENCION: ESTE PASO ES OBLIGATORIO EN TU SETUP.
--  ------------------------------------------------------------
--  Tu sistema usa:
--     - MySQL Server 8.0.46
--     - PHP 7.1.11 corriendo en IIS via FastCGI
--
--  MySQL 8.0 usa por defecto el plugin de autenticacion
--  "caching_sha2_password", que PHP 7.1 NO soporta nativamente
--  (recien se soporta a partir de PHP 7.4).
--
--  Si no aplicas este script, cualquier conexion mysqli() desde
--  PHP fallara con el error:
--     mysqli::__construct(): The server requested authentication
--     method unknown to the client [caching_sha2_password]
--
--  El profe del PDF de instalacion usa MariaDB 10.2, donde este
--  problema NO existe (MariaDB nunca adopto caching_sha2 como
--  default). Por eso el problema no aparece en su guia: aparece
--  porque vos usaste MySQL en vez de MariaDB.
-- ============================================================

ALTER USER 'root'@'localhost'
    IDENTIFIED WITH mysql_native_password BY 'Mamacita.com921';

FLUSH PRIVILEGES;

SELECT 'Usuario root ahora usa mysql_native_password. PHP 7.1 puede conectar.' AS resultado;
