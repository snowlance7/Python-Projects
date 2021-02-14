CREATE TABLE IF NOT EXIST Session (
 sessionID INTEGER PRIMARY KEY NOT NULL,
 startTime TEXT NOT NULL,
 startMoney REAL NOT NULL,
 addedMoney REAL NOT NULL,
 stopTime TEXT NOT NULL,
 stopMoney REAL NOT NULL
); 