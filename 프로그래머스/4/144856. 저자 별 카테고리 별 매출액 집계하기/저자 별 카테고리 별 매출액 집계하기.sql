-- 집계함수 밖으로 나간 연산은 group by의 영향을 받지 않는다 (sum(s.SALES)*b.PRICE) 하면 안댐
SELECT a.AUTHOR_ID,	a.AUTHOR_NAME,	b.CATEGORY,	sum(s.SALES*b.PRICE) as TOTAL_SALES
    from BOOK b
        join AUTHOR a
        on b.AUTHOR_ID = a.AUTHOR_ID
        join BOOK_SALES s
        on b.BOOK_ID = s.BOOK_ID
    where year(s.SALES_DATE) = '2022' and month(s.SALES_DATE) = '01'
    group by 1,2,3
    order by b.AUTHOR_ID, b.CATEGORY desc