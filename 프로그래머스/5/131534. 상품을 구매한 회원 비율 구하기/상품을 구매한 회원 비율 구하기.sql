-- 코드를 입력하세요 상품 테이블은 없는듯
with tbl as (SELECT 
    YEAR(sales_date) as YEAR, 
    MONTH(sales_date) AS MONTH, 
    COUNT(DISTINCT(j.USER_ID)) as PUCHASED_USERS
    from ONLINE_SALE o
        join (select * from USER_INFO where YEAR(JOINED) = '2021') j
        on o.USER_ID = j.USER_ID
    group by YEAR, MONTH)
, mm as (
    select count(*)
    from USER_INFO 
    where YEAR(JOINED) = "2021"
)

select YEAR, MONTH, 
    PUCHASED_USERS,
    ROUND(PUCHASED_USERS/(select * from mm),1) as PUCHASED_RATIO
    from tbl
    group by YEAR, MONTH
    order by YEAR, MONTH
