CREATE TABLE employees(
   id SERIAL PRIMARY KEY,
   name VARCHAR NOT NULL,
   salary INTEGER NOT NULL,
   currency VARCHAR NOT NULL,
   department VARCHAR NOT NULL,
   sub_department VARCHAR NOT NULL,
   on_contract INTEGER DEFAULT 0
);


