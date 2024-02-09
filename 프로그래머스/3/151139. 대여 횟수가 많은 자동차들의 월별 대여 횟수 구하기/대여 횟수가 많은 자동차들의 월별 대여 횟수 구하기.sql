select month(start_date) as month, car_id, count(history_id) as records
from car_rental_company_rental_history
where car_id in (
    select car_id
    from car_rental_company_rental_history
    where year(start_date)=2022 and month(start_date) between 8 and 10
    group by car_id
    having count(car_id) >= 5)
and year(start_date)=2022 and month(start_date) between 8 and 10
group by month, car_id
order by month, car_id desc