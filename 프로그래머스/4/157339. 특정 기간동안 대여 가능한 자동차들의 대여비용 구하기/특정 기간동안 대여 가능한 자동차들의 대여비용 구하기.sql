select c.CAR_ID, c.CAR_TYPE, ROUND(daily_fee*30 - daily_fee*30*DISCOUNT_RATE/100) as FEE
    from CAR_RENTAL_COMPANY_CAR c
        left join CAR_RENTAL_COMPANY_RENTAL_HISTORY h
        on c.CAR_ID = h.CAR_ID
        join CAR_RENTAL_COMPANY_DISCOUNT_PLAN p
        on c.CAR_TYPE = p.CAR_TYPE
    WHERE C.CAR_ID NOT IN (
    SELECT CAR_ID
    FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
    WHERE END_DATE > '2022-11-01' AND START_DATE < '2022-12-01'
) AND P.DURATION_TYPE='30일 이상'
    group by c.CAR_ID
    having c.CAR_TYPE in ("세단", "SUV")
        and 500000 <= FEE
        and 2000000 > FEE
    order by FEE desc, c.CAR_TYPE, c.CAR_ID desc