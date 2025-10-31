with recursive hours as (
    select 0 as hr
    union all
    select hr + 1 from hours where hr < 23
)
SELECT h.hr as HOUR, count(a.animal_id) as COUNT
from hours h
left join animal_outs a
on h.hr = hour(a.datetime)
group by h.hr
order by h.hr