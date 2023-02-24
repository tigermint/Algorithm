-- 코드를 입력하세요
select flavor
from (
    select A.flavor, A.sum + B.sum as sum
    from (
        select flavor, sum(total_order) as sum
        from july
        group by flavor
        ) A
        inner join
        (
            select flavor, sum(total_order) as sum
        from first_half
        group by flavor
        ) B on A.flavor = B.flavor
        order by A.sum + B.sum desc
)
where rownum <= 3

