-- 코드를 입력하세요
SELECT m.member_name, r.review_text, TO_CHAR(r.review_date, 'YYYY-MM-DD') AS review_date
FROM member_profile M, rest_review R, 
(select member_id
from (select count(*) as count, member_id from rest_review group by member_id) A,
(select max(count(*)) as count from rest_review group by member_id) B
where A.count = B.count
) T
WHERE M.member_id = T.member_id
and M.member_id = R.member_id
ORDER BY r.review_date,  r.review_text


