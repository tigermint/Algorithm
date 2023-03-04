-- 코드를 입력하세요
SELECT order_id
, PRODUCT_ID
, to_char(out_date, 'YYYY-MM-DD') as out_date
, CASE
        WHEN out_date <= to_date('2022-05-01' , 'YYYY-MM-DD') THEN '출고완료'
        WHEN out_date is null THEN '출고미정'
        ELSE '출고대기'
    END as 출고여부
from FOOD_ORDER
where 1=1
order by order_id