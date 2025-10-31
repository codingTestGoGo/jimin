-- 코드를 입력하세요
select INGREDIENT_TYPE, sum(b.total_order)
from icecream_info as a
join (
        select flavor, sum(total_order) as total_order
        from first_half
        group by flavor
    ) as b
on a.flavor = b.flavor
group by ingredient_type
order by b.total_order
