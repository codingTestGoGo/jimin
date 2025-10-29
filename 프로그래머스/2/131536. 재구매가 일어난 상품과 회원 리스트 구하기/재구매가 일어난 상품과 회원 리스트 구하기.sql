-- 코드를 입력하세요
# SELECT distinct a.USER_ID, a.PRODUCT_ID
# FROM ONLINE_SALE as a, ONLINE_SALE as b
# where a.user_id = b.user_id and a.product_id = b.product_id
# order by a.user_id, a.product_id desc

select user_id, product_id
from online_sale
group by user_id, product_id
having count(*) >= 2
order by user_id, product_id desc