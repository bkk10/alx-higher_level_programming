-- computing average of the records
-- use avg()

alter table second_table add average FLOAT;

select avg(score) from second_table;
