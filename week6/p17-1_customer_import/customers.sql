-- Drop the tables if they already exist in order to start with a fresh
-- database. You will lose any movies you added.

DROP TABLE IF EXISTS Customer;

-- Create Customer table
CREATE TABLE Customer(
    customerID  INTEGER PRIMARY KEY     NOT NULL,
    firstName   TEXT                    NOT NULL,
    lastName    TEXT                    NOT NULL,
    companyName TEXT                    NULL,
    address     TEXT                    NULL,
    city        TEXT                    NULL,
    state       TEXT                    NULL,
    zip         TEXT                    NULL
);

-- Populate the Customer table
INSERT INTO Customer VALUES (101,"James","Butler","","6649 N Blue Gum St","New Orleans","LA","70116");