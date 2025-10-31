select year(differentiation_date) as year, M - size_of_colony as year_dev, id
from ecoli_data as a
join(select year(differentiation_date) as year, max(size_of_colony) as M
     from ecoli_data
    group by year(differentiation_date)) as t
on year(differentiation_date) = t.year
order by year, year_dev