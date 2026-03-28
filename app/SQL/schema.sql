-- Drop in reverse order to respect FK dependencies
DROP TABLE IF EXISTS transaction_unit;
DROP TABLE IF EXISTS transaction;
DROP TABLE IF EXISTS buyer;
DROP TABLE IF EXISTS unit;
DROP TABLE IF EXISTS seller;
DROP TABLE IF EXISTS variant;
DROP TABLE IF EXISTS model;
DROP TABLE IF EXISTS product;
DROP TABLE IF EXISTS location;


CREATE TABLE location (
    lid     SERIAL PRIMARY KEY,
    name    VARCHAR(100) NOT NULL,  -- "Warehouse A", "Store NYC"
    address TEXT
);

CREATE TABLE product (
    pid   SERIAL PRIMARY KEY,
    brand VARCHAR(50) NOT NULL  -- Apple, Samsung, Google
);

CREATE TABLE model (
    mid   SERIAL PRIMARY KEY,
    pid   INT NOT NULL REFERENCES product(pid),
    name  VARCHAR(100) NOT NULL  -- "iPhone 17 Pro"
);

CREATE TABLE variant (
    vid     SERIAL PRIMARY KEY,
    mid     INT NOT NULL REFERENCES model(mid),
    SKU     VARCHAR(50),
    color   VARCHAR(50),         -- "Black"
    storage VARCHAR(20)          -- "256GB"
);

CREATE TABLE seller (
    sid   SERIAL PRIMARY KEY,
    name  VARCHAR(100) NOT NULL,
    phone VARCHAR(20),
    email VARCHAR(100)
);

CREATE TABLE unit (
    uid  SERIAL PRIMARY KEY,
    vid  INT NOT NULL REFERENCES variant(vid),
    lid  INT NOT NULL REFERENCES location(lid),
    sid  INT NOT NULL REFERENCES seller(sid),  -- where did this unit come from
    status VARCHAR(20) NOT NULL DEFAULT 'available' -- 'sold','available','blacklisted'
);


CREATE TABLE buyer (
    bid   SERIAL PRIMARY KEY,
    name  VARCHAR(100) NOT NULL,
    phone VARCHAR(20),
    email VARCHAR(100)
);

CREATE TABLE transaction (
    tid      SERIAL PRIMARY KEY,
    bid      INT NOT NULL REFERENCES buyer(bid),
    price    NUMERIC(10, 2) NOT NULL,  -- total sale price
    sold_at  TIMESTAMP DEFAULT NOW()
);

-- Stores many to many relationship of transactions and the units sold 
CREATE TABLE transaction_unit (
    tid  INT NOT NULL REFERENCES transaction(tid),
    uid  INT NOT NULL REFERENCES unit(uid),
    PRIMARY KEY (tid, uid)  -- composite PK, a unit can't appear twice in same transaction
);