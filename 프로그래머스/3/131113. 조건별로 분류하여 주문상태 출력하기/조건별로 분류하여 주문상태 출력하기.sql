-- 코드를 입력하세요
SELECT ORDER_ID, PRODUCT_ID, DATE_FORMAT(OUT_DATE, "%Y-%m-%d") as OUT_DATE,
    case when OUT_DATE is NULL then "출고미정"
        when DATEDIFF("2022-05-01", OUT_DATE) >= 0 then "출고완료"
        when DATEDIFF("2022-05-01", OUT_DATE) < 0 then "출고대기"
        end as "출고여부"
    from FOOD_ORDER 
    order by ORDER_ID