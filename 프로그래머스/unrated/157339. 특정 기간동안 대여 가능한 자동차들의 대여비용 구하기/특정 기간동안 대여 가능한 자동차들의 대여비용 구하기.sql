-- 코드를 입력하세요
SELECT DISTINCT C.car_id, 
C.car_type, 
ROUND(C.DAILY_FEE*30*(100-P.DISCOUNT_RATE)/100) AS fee
FROM CAR_RENTAL_COMPANY_CAR C 
JOIN CAR_RENTAL_COMPANY_RENTAL_HISTORY H ON C.car_id = H.car_id
JOIN CAR_RENTAL_COMPANY_DISCOUNT_PLAN P ON C.car_type = P.car_type
WHERE C.car_id NOT IN (
    SELECT DISTINCT car_id
    FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
    WHERE TO_CHAR(start_date, 'yyyy-mm-dd') BETWEEN '2022-11-01' AND '2022-11-30'
    OR TO_CHAR(end_date, 'yyyy-mm-dd') BETWEEN '2022-11-01' AND '2022-11-30'         
    OR (TO_CHAR(start_date, 'yyyy-mm-dd') <= '2022-11-01' AND TO_CHAR(end_date, 'yyyy-mm-dd') >= '2022-11-30')
)
AND P.duration_type = '30일 이상'
AND C.car_type IN ('세단', 'SUV')
AND ROUND(C.DAILY_FEE*30*(100-P.DISCOUNT_RATE)/100) BETWEEN 500000 AND 1999999
ORDER BY fee desc, C.car_type, C.car_id desc