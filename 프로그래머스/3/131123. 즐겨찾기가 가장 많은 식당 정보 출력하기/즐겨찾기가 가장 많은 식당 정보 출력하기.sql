-- 코드를 입력하세요
select FOOD_TYPE,	REST_ID,	REST_NAME,	FAVORITES
from rest_info
where (FOOD_TYPE, FAVORITES) in (
    select FOOD_TYPE, max(FAVORITES) as FAVORITES
    from rest_info
    group by FOOD_TYPE
)
order by FOOD_TYPE desc
