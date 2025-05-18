-- creates table unique_id
-- row id, name

create table if not exists unique_id(
	id INT default 1 unique,
	name VARCHAR(256));
