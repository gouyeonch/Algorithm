-- 코드를 입력하세요 0329
SELECT year(o.sales_date) "YEAR", month(o.sales_date) "MONTH", u.GENDER, count(DISTINCT o.USER_ID) "USERS"
    from ONLINE_SALE o
        join USER_INFO  u
        on o.USER_ID = u.USER_ID
    where GENDER is not NULL
    group by YEAR, MONTH, GENDER
    order by YEAR, MONTH, GENDER