-- 코드를 입력하세요
select animal_id, name
from animal_outs
minus
select animal_id, name
from animal_ins