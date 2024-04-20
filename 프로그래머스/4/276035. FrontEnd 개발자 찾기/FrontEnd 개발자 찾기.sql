-- 코드를 작성해주세요
SELECT DISTINCT d.id, d.email, d.first_name, d.last_name
FROM developers d JOIN skillcodes s
WHERE s.category = 'Front End'
AND s.code & d.skill_code = s.code
ORDER BY d.id;