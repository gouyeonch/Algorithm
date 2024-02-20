-- 코드를 입력하세요
SELECT HISTORY_ID, CAR_ID, DATE_FORMAT(START_DATE, "%Y-%m-%d") as START_DATE, DATE_FORMAT(END_DATE, "%Y-%m-%d") as END_DATE,
    if(DATEDIFF(END_DATE, START_DATE) < 29, "단기 대여", "장기 대여") as RENT_TYPE
    from CAR_RENTAL_COMPANY_RENTAL_HISTORY 
    where year(START_DATE) = "2022" and month(START_DATE) = "9"
    order by HISTORY_ID desc