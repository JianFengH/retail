CREATE DATABASE IF NOT EXISTS retail;

USE retail;

CREATE TABLE Shop (

   shop_id varchar(30),

   name varchar(50) NOT NULL,

   rating integer,

   location varchar(200),

   PRIMARY KEY(shop_id)

);



CREATE TABLE Item (

   item_id varchar(30),

   shop_id varchar(30) NOT NULL,

   name varchar(50) NOT NULL,

   price float NOT NULL,

   stock integer NOT NULL,

   keyword1 varchar(20),

   keyword2 varchar(20),

   keyword3 varchar(20),

   PRIMARY KEY(item_id),

   FOREIGN KEY(shop_id) REFERENCES Shop(shop_id)

);



CREATE TABLE Customer (

   customer_id varchar(30),

   name varchar(50) NOT NULL,

   phone varchar(15),

   address varchar(200),

   PRIMARY KEY(customer_id) 

);



CREATE TABLE Order1 (

   order_id varchar(30),

   customer_id varchar(30) NOT NULL,

   status varchar(20) NOT NULL,

   date DATETIME NOT NULL,

   PRIMARY KEY(order_id),

   FOREIGN KEY(customer_id) REFERENCES Customer(customer_id)

);



CREATE TABLE Detail (

   detail_id varchar(30),

   order_id varchar(30) NOT NULL,

   item_id varchar(30) NOT NULL,

   item_count varchar(30) NOT NULL,

   status varchar(20) NOT NULL,

   PRIMARY KEY(detail_id),

   FOREIGN KEY(order_id) REFERENCES Order1(order_id),

   FOREIGN KEY(item_id) REFERENCES Item(item_id)

);


CREATE TRIGGER ORDER_DETAIL_INSERT

AFTER INSERT ON Detail

FOR EACH ROW

BEGIN

   UPDATE Item SET stock = stock - NEW.item_count WHERE item_id = NEW.item_id;

END;



CREATE TRIGGER ORDER_DETAIL_UPDATE_STATUS_CANCELED

AFTER UPDATE ON Detail

FOR EACH ROW

BEGIN

   IF (OLD.status <> NEW.status AND NEW.status = 'canceled') THEN

       UPDATE Item SET stock = stock + NEW.item_count WHERE item_id = NEW.item_id;

   END IF;

END;



INSERT INTO `Shop` (`shop_id`, `name`, `rating`, `location`) VALUES
('3465421', 'PASER', 43, 'Makuu'),
('7896233', 'LEMENT', 3, 'Hong Kong'),
('6239568', 'Round Stic', 6, 'UK'),
('5471083', 'Apple', 1, 'USA'),
('9823640', 'ONKYO', 10, 'Hong Kong');

INSERT INTO `Item` (`item_id`, `shop_id`, `name`, `price`, `stock`, `keyword1`, `keyword2`,`keyword3`) VALUES
('210028-10', '3465421', 'PASER Motivational Water Bottle', '17.99', '500', 'Sports','Outdoors','Water Bottles'),
('456234-34', '7896233', 'KN95 Face Mask', '13.89', '500', 'Safety','Respirators','Masks'),
('897128-46', '6239568', 'BIC Round Ballpoint Pen', '9.96', '500', 'Office','School','Pens'),
('901831-01', '5471083', 'Apple AirPods Pro', '224.99', '500', 'Apple','Wireless','AirPods'),
('332858-71', '9823640', 'ONKYO Bluetooth Mini Projector', '186.98', '500', 'Electronics','Movie','Video Projectors');

INSERT INTO `Customer` (`customer_id`, `name`, `phone`, `address`) VALUES
('3465474', 'Jane Smith', '684-324-4534', '11501 Domain, DR #110'),
('2356732', 'Christy Klingler', '456-325-6980', '14390 Chantilly, VA 20151'),
('6783456', 'Joan Johnson', '785-320-1246', '34623 Madison, SD 57042'),
('9756101', 'Tony Notreal', '976-583-1789', '12340 Washington, DC 22002');

INSERT INTO `Order1` (`order_id`, `customer_id`, `status`, `date`) VALUES
('701-9923802-8100257', '3465474', 'pending', '2022-04-15 03:34:00'),
('546-3576579-6423232', '2356732', 'completed', '2022-04-14 08:12:00'),
('867-9203244-9627115', '6783456', 'canceled', '2022-03-01 10:11:00'),
('652-2488071-1267903', '9756101', 'unshipped', '2022-04-18 01:20:00'),
('891-9717621-9732781', '2356732', 'shipped', '2022-03-10 06:39:00');

INSERT INTO `Detail` (`detail_id`, `order_id`, `item_id`, `item_count`,`status`) VALUES
('00000032', '701-9923802-8100257', '210028-10', 2, 'created'),
('00000345', '546-3576579-6423232', '456234-34', 50, 'created'),
('00000078', '867-9203244-9627115', '897128-46', 36, 'canceled'),
('00000065', '652-2488071-1267903', '901831-01', 1, 'created'),
('00000090', '891-9717621-9732781', '332858-71', 1, 'created');
