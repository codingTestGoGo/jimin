-- 코드를 작성해주세요
select a.id, b.fish_name, a.length
from fish_info a
join fish_name_info b
on a.fish_type = b.fish_type
where a.length = (select max(c.length) from fish_info c where a.fish_type = c.fish_type)
order by a.id
