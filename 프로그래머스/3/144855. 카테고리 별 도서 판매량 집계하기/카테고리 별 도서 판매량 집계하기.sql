-- 코드를 입력하세요
SELECT CATEGORY,	sum(s.SALES) as TOTAL_SALES
    from BOOK b
        join BOOK_SALES s
        on b.BOOK_ID = s.BOOK_ID
    where year(s.SALES_DATE) = '2022' 
        and month(s.SALES_DATE) = '01'
    group by b.CATEGORY
    order by b.CATEGORY