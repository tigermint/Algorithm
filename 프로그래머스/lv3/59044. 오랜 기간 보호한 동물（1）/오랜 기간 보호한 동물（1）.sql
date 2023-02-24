-- 코드를 입력하세요
select name, datetime
from (
    select *
    from (
        select I.animal_id
        from animal_ins I left outer join animal_outs O on I.animal_id = O.animal_id
        minus
        select animal_id
        from animal_outs
    ) A inner join animal_ins B on A.animal_id = B.animal_id
    order by datetime
)
where rownum <= 3