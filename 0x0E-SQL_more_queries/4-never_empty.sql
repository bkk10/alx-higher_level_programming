-- create a table id_not_null
-- row: id, name

create table if not exists id_not_null(
	id INT default 1,
	name VARCHAR(256));
