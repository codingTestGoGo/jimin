-- 코드를 작성해주세요
select concat(length,'cm') as max_length
from fish_info
where length = (select max(length) from fish_info)