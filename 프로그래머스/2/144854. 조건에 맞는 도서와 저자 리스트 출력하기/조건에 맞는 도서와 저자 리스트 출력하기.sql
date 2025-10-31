SELECT b.BOOK_ID, a.AUTHOR_NAME, date_format(b.PUBLISHED_DATE,'%Y-%m-%d') as PUBLISHED_DATE
from book b
join author a
on a.author_id = b.author_id
where b.category = '경제'
order by b.published_date