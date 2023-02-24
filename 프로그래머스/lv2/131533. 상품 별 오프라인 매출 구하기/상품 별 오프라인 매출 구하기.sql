-- 코드를 입력하세요
select P.product_code, sum(P.PRICE * O.SALES_AMOUNT) as sales
from product P, offline_sale O
where P.product_id = O.product_id
group by P.product_code
order by sales desc, P.product_code asc
