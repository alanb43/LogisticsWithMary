PRAGMA foreign_keys = ON;
CREATE TABLE users(
  userid INTEGER PRIMARY KEY AUTOINCREMENT,
  username VARCHAR(20),
  password VARCHAR(256)
);

-- DATES STORED AS STRINGS OF FORMAT YYYYMMDD
CREATE TABLE unfulfilled(
  orderid INTEGER PRIMARY KEY AUTOINCREMENT,
  name VARCHAR(20),
  clothingarticle VARCHAR(32),
  size VARCHAR(10),
  color VARCHAR(16),
  design VARCHAR(128),
  orderedorstocked VARCHAR(32),
  pricecharged VARCHAR(16),
  paid VARCHAR(8),
  shipped VARCHAR(8),
  shippingaddress VARCHAR(128),
  completeby VARCHAR(32),
  notes VARCHAR(128),
  created INTEGER
);

-- DATES STORED AS STRINGS OF FORMAT YYYYMMDD
CREATE TABLE fulfilled(
  fulfilledid INTEGER PRIMARY KEY AUTOINCREMENT,
  name VARCHAR(20),
  clothingarticle VARCHAR(32),
  size VARCHAR(10),
  color VARCHAR(16),
  design VARCHAR(128),
  pricecharged VARCHAR(16),
  shipped VARCHAR(8),
  shippingaddress VARCHAR(128),
  notes VARCHAR(128),
  fulfilledat INTEGER
);

CREATE TABLE inventory(
  itemid INTEGER PRIMARY KEY AUTOINCREMENT,
  brand VARCHAR(32),
  clothingarticle VARCHAR(64),
  size VARCHAR(64),
  color VARCHAR(64),
  quantity INTEGER,
  personaluse VARCHAR(128)
);
