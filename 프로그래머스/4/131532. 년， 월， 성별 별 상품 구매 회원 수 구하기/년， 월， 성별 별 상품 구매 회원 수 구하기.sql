select 
    YEAR(sales_date) as YEAR, 
    MONTH(sales_date) as MONTH,
    GENDER,
    count(DISTINCT s.USER_ID) as USERS
    from ONLINE_SALE s
        join USER_INFO u
        on s.USER_ID = u.USER_ID
    where u.GENDER is not NULL
    group by YEAR, MONTH, GENDER
    order by YEAR, MONTH, GENDER