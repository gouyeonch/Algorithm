select DISTINCT(C.CAR_ID), C.CAR_TYPE, ROUND(DAILY_FEE * 30 - (DAILY_FEE * 30 * (DISCOUNT_RATE/100))) AS FEE
    from CAR_RENTAL_COMPANY_CAR c
        left join CAR_RENTAL_COMPANY_RENTAL_HISTORY h
        on c.CAR_ID = h.CAR_ID
        join CAR_RENTAL_COMPANY_DISCOUNT_PLAN p
        on c.CAR_TYPE = p.CAR_TYPE
    where DURATION_TYPE = "30일 이상"
        and 500000 <= ROUND(daily_fee*30 - daily_fee*30*DISCOUNT_RATE/100)
        and 2000000 > ROUND(daily_fee*30 - daily_fee*30*DISCOUNT_RATE/100)
        and c.CAR_TYPE in ("세단", "SUV")
        and c.CAR_ID not in (
            select CAR_ID
                from CAR_RENTAL_COMPANY_RENTAL_HISTORY 
                where END_DATE > '2022-11-01' AND START_DATE < '2022-11-30')
    order by FEE desc, c.CAR_TYPE, c.CAR_ID desc