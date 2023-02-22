-- 코드를 입력하세요
SELECT b.book_id, a.author_name, TO_CHAR(B.PUBLISHED_DATE, 'YYYY-MM-DD') as published_date
FROM book b join author a ON b.author_id = a.author_id
WHERE b.category = '경제'
ORDER BY b.published_date 