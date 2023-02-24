-- 코드를 입력하세요
select A.product_id, B.product_name, A.amount_per_product * B.price as total_sales
from (
    select product_id, sum(amount) as amount_per_product
    from food_order
    where to_char(produce_date, 'yyyy-mm') = '2022-05'
    group by product_id
) A join food_product B on A.product_id = B.product_id
order by A.amount_per_product * B.price desc, A.product_id
