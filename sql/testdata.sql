INSERT INTO users(username, password)
VALUES('alan', 'alan');

-- UNFULFILLED TABLE
INSERT INTO unfulfilled(
    name, clothingarticle, size, color, design, orderedorstocked,
    pricecharged, shipped, shippingaddress, completeby, notes, created)
VALUES(
    'alan', 'hoodie', 'L', 'brown', 'travisscott', 'need to order', '$60', 
    'no', '12345 Wallabye Way', '03/20/2022', 'order design from shop', '2022-10-12');
INSERT INTO unfulfilled(
    name, clothingarticle, size, color, design, orderedorstocked,
    pricecharged, shipped, shippingaddress, completeby, notes, created)
VALUES(
    'bella', 'hoodie', 'S', 'grey', 'travisscott', 'ordered', '$60', 
    'no', '12345 Wallabye Way', '03/20/2022', 'order design from shop', '2022-10-12');
INSERT INTO unfulfilled(
    name, clothingarticle, size, color, design, orderedorstocked,
    pricecharged, shipped, shippingaddress, completeby, notes, created)
VALUES(
    'alan', 'hoodie', 'L', 'brown', 'travisscott', 'need to order', '$60', 
    'no', '12345 Wallabye Way', '03/20/2022', 'order design from shop', '2022-10-12');
INSERT INTO unfulfilled(
    name, clothingarticle, size, color, design, orderedorstocked,
    pricecharged, shipped, shippingaddress, completeby, notes, created)
VALUES(
    'bella', 'hoodie', 'S', 'grey', 'travisscott', 'ordered', '$60', 
    'no', '12345 Wallabye Way', '03/20/2022', 'order design from shop', '2022-10-12');
INSERT INTO unfulfilled(
    name, clothingarticle, size, color, design, orderedorstocked,
    pricecharged, shipped, shippingaddress, completeby, notes, created)
VALUES(
    'alan', 'hoodie', 'L', 'brown', 'travisscott', 'need to order', '$60', 
    'no', '12345 Wallabye Way', '03/20/2022', 'order design from shop', '2022-10-12');
INSERT INTO unfulfilled(
    name, clothingarticle, size, color, design, orderedorstocked,
    pricecharged, shipped, shippingaddress, completeby, notes, created)
VALUES(
    'bella', 'hoodie', 'S', 'grey', 'travisscott', 'ordered', '$60', 
    'no', '12345 Wallabye Way', '03/20/2022', 'order design from shop', '2022-10-12');
INSERT INTO unfulfilled(
    name, clothingarticle, size, color, design, orderedorstocked,
    pricecharged, shipped, shippingaddress, completeby, notes, created)
VALUES(
    'alan', 'hoodie', 'L', 'brown', 'travisscott', 'need to order', '$60', 
    'no', '12345 Wallabye Way', '03/20/2022', 'order design from shop', '2022-10-12');
INSERT INTO unfulfilled(
    name, clothingarticle, size, color, design, orderedorstocked,
    pricecharged, shipped, shippingaddress, completeby, notes, created)
VALUES(
    'bella', 'hoodie', 'S', 'grey', 'travisscott', 'ordered', '$60', 
    'no', '12345 Wallabye Way', '03/20/2022', 'order design from shop', '2022-10-12');
INSERT INTO unfulfilled(
    name, clothingarticle, size, color, design, orderedorstocked,
    pricecharged, shipped, shippingaddress, completeby, notes, created)
VALUES(
    'alan', 'hoodie', 'L', 'brown', 'travisscott', 'need to order', '$60', 
    'no', '12345 Wallabye Way', '03/20/2022', 'order design from shop', '2022-10-12');
INSERT INTO unfulfilled(
    name, clothingarticle, size, color, design, orderedorstocked,
    pricecharged, shipped, shippingaddress, completeby, notes, created)
VALUES(
    'bella', 'hoodie', 'S', 'grey', 'travisscott', 'ordered', '$60', 
    'no', '12345 Wallabye Way', '03/20/2022', 'order design from shop', '2022-10-12');
INSERT INTO unfulfilled(
    name, clothingarticle, size, color, design, orderedorstocked,
    pricecharged, shipped, shippingaddress, completeby, notes, created)
VALUES(
    'alan', 'hoodie', 'L', 'brown', 'travisscott', 'need to order', '$60', 
    'no', '12345 Wallabye Way', '03/20/2022', 'order design from shop', '2022-10-12');
INSERT INTO unfulfilled(
    name, clothingarticle, size, color, design, orderedorstocked,
    pricecharged, shipped, shippingaddress, completeby, notes, created)
VALUES(
    'bella', 'hoodie', 'S', 'grey', 'travisscott', 'ordered', '$60', 
    'no', '12345 Wallabye Way', '03/20/2022', 'order design from shop', '2022-10-12');

-- FULFILLED TABLE
INSERT INTO fulfilled(
    name, clothingarticle, size, color, design,
    pricecharged, shipped, shippingaddress, notes, fulfilledat)
VALUES(
    'bella', 'crewneck', 'L', 'blue', 'anime design', '$60', 'not yet shipped', 
    '12345 Wallabye Way', 'need to print shipping label', '2022-10-12');

-- INVENTORY TABLE
INSERT INTO inventory(brand, clothingarticle, size, color, quantity, personaluse)
VALUES('comfort colors', 'hoodie', 'XXL', 'blue', 6, 'no');
INSERT INTO inventory(brand, clothingarticle, size, color, quantity, personaluse)
VALUES('gildan', 'tee-shirt', 'M', 'purple', 1, 'yes');
INSERT INTO inventory(brand, clothingarticle, size, color, quantity, personaluse)
VALUES('comfort colors', 'crewneck', 'S', 'red', 3, 'no');
INSERT INTO inventory(brand, clothingarticle, size, color, quantity, personaluse)
VALUES('gildan', 'tee', 'M', 'blue', 15, 'no');
INSERT INTO inventory(brand, clothingarticle, size, color, quantity, personaluse)
VALUES('comfort colors', 'hoodie', 'L', 'orange', 15, 'no');
