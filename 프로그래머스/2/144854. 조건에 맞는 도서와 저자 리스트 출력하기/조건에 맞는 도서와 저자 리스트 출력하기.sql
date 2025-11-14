-- 코드를 입력하세요
SELECT b.book_id, a.author_name, to_char(b.published_date, 'yyyy-mm-dd')
from book b
join author a
on a.author_id = b.author_id
where category = '경제'
order by b.published_date