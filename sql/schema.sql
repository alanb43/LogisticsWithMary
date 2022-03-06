PRAGMA foreign_keys = ON;
CREATE TABLE users(
  username VARCHAR(20) PRIMARY KEY,
  password VARCHAR(256),
);

CREATE TABLE unfulfilled(
  orderid INTEGER PRIMARY KEY AUTOINCREMENT,
  name VARCHAR(20),
  clothingarticle VARCHAR(64),
  size VARCHAR(64),
  color VARCHAR(64),
  design VARCHAR(256),
  orderedorstocked VARCHAR(64),
  pricecharged VARCHAR(64),
  shipped VARCHAR(64),
  shippingaddress VARCHAR(512),
  completeby VARCHAR(128),
  created DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
);

CREATE TABLE fulfilled(
  fulfilledid INTEGER PRIMARY KEY AUTOINCREMENT,
  name VARCHAR(20),
  clothingarticle VARCHAR(64),
  size VARCHAR(64),
  color VARCHAR(64),
  design VARCHAR(256),
  pricecharged VARCHAR(64),
  shipped VARCHAR(64),
  shippingaddress VARCHAR(512),
  fulfilledat DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
);

CREATE TABLE inventory(
  itemid INTEGER PRIMARY KEY AUTOINCREMENT,
  brand VARCHAR(32),
  clothingarticle VARCHAR(64),
  size VARCHAR(64),
  color VARCHAR(64),
  quantity INTEGER,
  personaluse VARCHAR(128),
);
