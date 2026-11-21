-- Einmalig als root ausführen: legt Datenbank und Benutzer für KickerRank an.
-- Terminal:  mysql -u root -p < docs/setup.sql
-- Oder in MySQL Workbench öffnen und ausführen.
-- Das Skript kann mehrmals ausgeführt werden.

CREATE DATABASE IF NOT EXISTS kickerrank
CHARACTER SET utf8mb4;

-- Benutzer neu anlegen, damit nur die Rechte unten gelten (auch wenn er schon existierte).
DROP USER IF EXISTS 'kicker'@'localhost';
CREATE USER 'kicker'@'localhost' IDENTIFIED BY 'kicker';

-- Nur die Rechte, welche die App braucht, und nur auf die Datenbank kickerrank:
--   SELECT, INSERT, UPDATE, DELETE  Daten lesen und ändern
--   CREATE, REFERENCES              Tabellen mit Fremdschlüsseln beim ersten Start anlegen
GRANT SELECT, INSERT, UPDATE, DELETE, CREATE, REFERENCES
    ON kickerrank.* TO 'kicker'@'localhost';
