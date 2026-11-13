-- Einmalig als root ausführen: legt Datenbank und Benutzer für KickerRank an.
-- Terminal:  mysql -u root -p < docs/setup.sql
-- Oder in MySQL Workbench öffnen und ausführen.

CREATE DATABASE IF NOT EXISTS kickerrank
    CHARACTER SET utf8mb4
    COLLATE utf8mb4_unicode_ci;

CREATE USER IF NOT EXISTS 'kicker'@'localhost' IDENTIFIED BY 'kicker';
GRANT ALL PRIVILEGES ON kickerrank.* TO 'kicker'@'localhost';
FLUSH PRIVILEGES;
