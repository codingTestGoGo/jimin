-- 코드를 입력하세요
SELECT  HISTORY_ID, 
        CAR_ID, to_char(START_DATE, 'YYYY-MM-DD') as START_DATE, 
        to_char(END_DATE, 'YYYY-MM-DD') as END_DATE,
        case 
            when (END_DATE - START_DATE + 1) >= 30 
            then '장기 대여' 
        else '단기 대여' end as RENT_TYPE
from CAR_RENTAL_COMPANY_RENTAL_HISTORY
WHERE TO_CHAR(START_DATE, 'YYYY-MM') = '2022-09'
order by history_id desc