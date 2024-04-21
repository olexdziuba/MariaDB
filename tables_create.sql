-- Table for storing client information
CREATE TABLE Clients (
    ClientID INTEGER UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    ClientName VARCHAR(20) NOT NULL,
    ClientAddress VARCHAR(50) NOT NULL,
    City VARCHAR(50) NOT NULL,
    PhoneNumber VARCHAR(15) NOT NULL
);

-- Table for storing article information
CREATE TABLE Articles (
    ArticleID INTEGER UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    ArticleDescription VARCHAR(20) NOT NULL,
    UnitPrice DECIMAL(10,2) NOT NULL,
    StockQuantity INTEGER UNSIGNED
);

-- Deleting unnecessary columns from Articles table
ALTER TABLE Articles
DROP COLUMN AuthorID, DROP COLUMN Year, DROP COLUMN GenreID;

-- Adding new columns to Articles table
ALTER TABLE Articles
ADD AuthorID INTEGER UNSIGNED NOT NULL AFTER ArticleDescription,
ADD Year INTEGER UNSIGNED NOT NULL AFTER AuthorID,
ADD GenreID INTEGER UNSIGNED NOT NULL AFTER Year;

-- Deleting a column from Articles table
ALTER TABLE Articles
DROP COLUMN AuthorID;

-- Modifying a column in Articles table
ALTER TABLE Articles
MODIFY StockQuantity INTEGER UNSIGNED NOT NULL;

-- Describing the structure of Articles table
DESCRIBE Articles;

-- Table for storing order information
CREATE TABLE Orders (
    OrderID INTEGER UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    OrderDate DATE NOT NULL,
    ClientID INTEGER UNSIGNED NOT NULL
);

-- Table for storing order line item information
CREATE TABLE OrderLines (
    OrderID INTEGER UNSIGNED NOT NULL,
    ArticleID INTEGER UNSIGNED NOT NULL,
    Quantity INTEGER UNSIGNED NOT NULL
);

-- Table for storing delivery information
CREATE TABLE Deliveries (
    DeliveryID INTEGER UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    DeliveryDate DATE NOT NULL
);

-- Table for storing delivery detail information
CREATE TABLE DeliveryDetails (
    DeliveryID INTEGER UNSIGNED NOT NULL,
    OrderID INTEGER UNSIGNED NOT NULL,
    ArticleID INTEGER UNSIGNED NOT NULL,
    DeliveredQuantity INTEGER UNSIGNED NOT NULL
);

-- Table for storing author information
CREATE TABLE Authors (
    AuthorID INTEGER UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    AuthorName VARCHAR(20) NOT NULL
);

-- Table for storing genre information
CREATE TABLE Genres (
    GenreID INTEGER UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    GenreDescription VARCHAR(20) NOT NULL
);

-- Table for storing shelf placement information
CREATE TABLE ShelfPlacements (
    ShelfID INTEGER UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    GenreID INTEGER UNSIGNED NOT NULL
);
