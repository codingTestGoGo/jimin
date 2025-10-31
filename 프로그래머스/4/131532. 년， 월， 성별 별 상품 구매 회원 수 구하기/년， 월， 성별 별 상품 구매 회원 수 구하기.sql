select year(a.sales_date) as `year`, month(sales_date) as `month`, b.gender, count(distinct a.user_id)
from online_sale a
join user_info b
on a.user_id = b.user_id
where b.gender is not null
group by year(a.sales_date), month(a.sales_date), b.gender
order by year(a.sales_date), month(a.sales_date), b.gender