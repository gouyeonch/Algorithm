-- 코드를 입력하세요
SELECT DISTINCT c.car_id
    from CAR_RENTAL_COMPANY_CAR  c
        join CAR_RENTAL_COMPANY_RENTAL_HISTORY h
        on c.car_id = h.car_id
    where car_type = "세단" 
        and month(h.START_DATE) = 10
    order by c.car_id desc