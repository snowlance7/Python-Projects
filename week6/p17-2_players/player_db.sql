-- *************************************************************
-- This script creates a database of players
-- *************************************************************

DROP TABLE IF EXISTS Player;

CREATE TABLE Player
(
  playerID      INTEGER        NOT NULL      PRIMARY KEY,
  name          TEXT           NOT NULL      UNIQUE,
  wins          INTEGER        NOT NULL,
  losses        INTEGER        NOT NULL,
  ties          INTEGER        NOT NULL
);

INSERT INTO Player VALUES 
(1,'Joel',3,7,10), 
(2,'Mike',4,3,7);