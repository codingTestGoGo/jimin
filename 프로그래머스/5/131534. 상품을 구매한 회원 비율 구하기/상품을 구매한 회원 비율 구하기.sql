select 
    extract(year from o.sales_date) as year,
    extract(month from o.sales_date) as month,
    count(distinct u.user_id) as purchased_users,
    round(
        count(distinct u.user_id)
        / (
            select count(*)
            from user_info ui
            where to_char(ui.joined, 'YYYY') = '2021'
        ),
        1
    ) as purchased_ratio
    
from user_info u
join online_sale o
    on u.user_id = o.user_id
where to_char(u.joined, 'YYYY') = '2021'
group by
    extract(year from o.sales_date),
    extract(month from o.sales_date)
order by
    year,
    month;