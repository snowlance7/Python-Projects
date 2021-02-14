-- *************************************************************
-- This script creates a database of tasks
-- *************************************************************

DROP TABLE IF EXISTS Task;

CREATE TABLE Task
(
  taskID      INTEGER        NOT NULL      PRIMARY KEY,
  description TEXT           NOT NULL,
  completed   INTEGER        NOT NULL
);

INSERT INTO Task VALUES 
(1,'Get bike fixed',1), 
(2,'Call your mom',1), 
(3,'Buy toothbrush',0), 
(4,'Do homework',0);