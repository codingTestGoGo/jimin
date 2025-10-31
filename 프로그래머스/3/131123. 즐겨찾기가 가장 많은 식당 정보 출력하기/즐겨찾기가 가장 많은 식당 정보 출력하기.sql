-- 코드를 입력하세요
SELECT a.food_type, a.rest_id, a.rest_name, t.favorites
from rest_info a
join (select food_type, max(favorites) as favorites
     from rest_info
     group by food_type) as t
on a.food_type = t.food_type
and a.favorites = t.favorites
# group by food_type
order by food_type desc
