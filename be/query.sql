CREATE SCHEMA inventory;

DROP TABLE IF EXISTS roles;
DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS items;
DROP TABLE IF EXISTS user_items;

CREATE TABLE roles (
  role_id SERIAL PRIMARY KEY,
  name text UNIQUE
);

CREATE TABLE users (
  user_id SERIAL PRIMARY KEY,
  role_id INT NOT NULL,
  fullname VARCHAR(50),
  username VARCHAR(20) NOT NULL,
  password TEXT NOT NULL,
  CONSTRAINT fk_role FOREIGN KEY(role_id) REFERENCES roles(role_id)
);

CREATE TABLE items(
  item_id SERIAL PRIMARY KEY,
  name VARCHAR(100) NOT NULL,
  description TEXT,
  quantity  INT NOT NULL DEFAULT 0
);

CREATE TABLE user_items (
  user_item_id SERIAL PRIMARY KEY,
  user_id INT NOT NULL,
  item_id INT NOT NULL,
  amount INT NOT NULL DEFAULT 0,
  CONSTRAINT fk_user_item FOREIGN KEY(user_id) REFERENCES users(user_id),
  CONSTRAINT fk_item FOREIGN KEY(item_id) REFERENCES items(item_id)
);
