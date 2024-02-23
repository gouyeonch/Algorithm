-- 코드를 입력하세요
with DUR as (SELECT HISTORY_ID,c.CAR_TYPE,
    (DATEDIFF(END_DATE, START_DATE)+1)*c.DAILY_FEE as REG_FEE, 
    case when DATEDIFF(END_DATE, START_DATE)+1 >= 90 then "90일 이상"
    when DATEDIFF(END_DATE, START_DATE)+1 >= 30 then "30일 이상"
    when DATEDIFF(END_DATE, START_DATE)+1 >= 7 then "7일 이상"
    else "미적용"
    end as DURATION
    from CAR_RENTAL_COMPANY_CAR c
        join CAR_RENTAL_COMPANY_RENTAL_HISTORY h
        on c.CAR_ID = h.CAR_ID
    where c.CAR_TYPE = '트럭'
    group by HISTORY_ID)

select HISTORY_ID, 
    if(plan_id is null, REG_FEE, ROUND(REG_FEE-(REG_FEE*p.discount_rate/100))) as FEE
    from DUR d
        left join CAR_RENTAL_COMPANY_DISCOUNT_PLAN p
        on d.DURATION = p.DURATION_TYPE
        and d.CAR_TYPE = p.CAR_TYPE
        
    order by FEE desc, HISTORY_ID desc