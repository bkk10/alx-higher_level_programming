-- showing name with score
-- displaying score in ascending order

select score, name
from second_table
where name is not null and name != ''
order by score desc;
