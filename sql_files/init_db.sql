-- Create the database
CREATE DATABASE marketplace_api;

-- Connect to the database
\c marketplace_api;

-- Create the tables

-- 1. Player Table
CREATE TABLE Player (
    player_id SERIAL PRIMARY KEY,
    username VARCHAR(50) NOT NULL UNIQUE,
    email VARCHAR(100) NOT NULL UNIQUE,
    password VARCHAR(100) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- 2. Item Table
CREATE TABLE Item (
    item_id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    description TEXT,
    category VARCHAR(50),
    rarity VARCHAR(50),
    price DECIMAL(10, 2) NOT NULL
);

-- 3. Inventory Table
CREATE TABLE Inventory (
    inventory_id SERIAL PRIMARY KEY,
    player_id INT REFERENCES Player(player_id) ON DELETE CASCADE,
    item_id INT REFERENCES Item(item_id) ON DELETE CASCADE,
    quantity INT NOT NULL,
    UNIQUE(player_id, item_id)  -- Ensure each item appears only once per player's inventory
);

-- 4. Listing Table
CREATE TABLE Listing (
    listing_id SERIAL PRIMARY KEY,
    item_id INT REFERENCES Item(item_id) ON DELETE CASCADE,
    seller_id INT REFERENCES Player(player_id) ON DELETE CASCADE,
    price DECIMAL(10, 2) NOT NULL,
    quantity INT NOT NULL,
    status VARCHAR(20) NOT NULL CHECK (status IN ('active', 'sold', 'cancelled')),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- 5. Transaction Table
CREATE TABLE Transaction (
    transaction_id SERIAL PRIMARY KEY,
    buyer_id INT REFERENCES Player(player_id) ON DELETE CASCADE,
    seller_id INT REFERENCES Player(player_id) ON DELETE CASCADE,
    item_id INT REFERENCES Item(item_id) ON DELETE CASCADE,
    listing_id INT REFERENCES Listing(listing_id) ON DELETE CASCADE,
    price DECIMAL(10, 2) NOT NULL,
    quantity INT NOT NULL,
    status VARCHAR(20) NOT NULL CHECK (status IN ('completed', 'failed')),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Indexes for performance
CREATE INDEX idx_inventory_player_id ON Inventory(player_id);
CREATE INDEX idx_inventory_item_id ON Inventory(item_id);
CREATE INDEX idx_listing_item_id ON Listing(item_id);
CREATE INDEX idx_listing_seller_id ON Listing(seller_id);
CREATE INDEX idx_transaction_buyer_id ON Transaction(buyer_id);
CREATE INDEX idx_transaction_seller_id ON Transaction(seller_id);
CREATE INDEX idx_transaction_item_id ON Transaction(item_id);
CREATE INDEX idx_transaction_listing_id ON Transaction(listing_id);
