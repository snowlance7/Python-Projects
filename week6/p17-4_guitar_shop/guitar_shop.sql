-- Drop the tables if they already exist in order to start with a fresh
-- database. You will lose any data you added.

DROP TABLE IF EXISTS Category;
DROP TABLE IF EXISTS Product;

-- create the tables
CREATE TABLE Category (
  categoryID       INTEGER PRIMARY KEY     NOT NULL,
  categoryName     TEXT                    NOT NULL
);

CREATE TABLE Product (
  productID        INTEGER PRIMARY KEY     NOT NULL,
  categoryID       INTEGER                 NOT NULL,
  productCode      TEXT UNIQUE             NOT NULL,
  productName      TEXT                    NOT NULL,
  listPrice        REAL                    NOT NULL
);

-- insert data into the database
INSERT INTO Category VALUES
(1, 'Guitars'),
(2, 'Basses'),
(3, 'Drums');

INSERT INTO Product VALUES
(1, 1, 'strat', 'Fender Stratocaster', '699.00'),
(2, 1, 'les_paul', 'Gibson Les Paul', '1199.00'),
(3, 1, 'sg', 'Gibson SG', '2517.00'),
(4, 1, 'fg700s', 'Yamaha FG700S', '489.99'),
(5, 1, 'washburn', 'Washburn D10S', '299.00'),
(6, 1, 'rodriguez', 'Rodriguez Caballero 11', '415.00'),
(7, 2, 'precision', 'Fender Precision', '799.99'),
(8, 2, 'hofner', 'Hofner Icon', '499.99'),
(9, 3, 'ludwig', 'Ludwig 5-piece Drum Set with Cymbals', '699.99'),
(10, 3, 'tama', 'Tama 5-Piece Drum Set with Cymbals', '799.99');