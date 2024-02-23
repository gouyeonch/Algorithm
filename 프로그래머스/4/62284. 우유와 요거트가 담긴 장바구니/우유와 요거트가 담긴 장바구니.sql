-- 코드를 입력하세요
with TBL as (SELECT *
    from CART_PRODUCTS 
    where NAME in ("Milk", "Yogurt")
    group by CART_ID, NAME)

select CART_ID
    from TBL
    group by CART_ID
    having count(*) = 2
    order by CART_ID