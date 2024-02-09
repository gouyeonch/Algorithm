-- 코드를 입력하세요
SELECT I.REST_ID,	I.REST_NAME,	I.FOOD_TYPE,	I.FAVORITES,	I.ADDRESS,	ROUND(AVG(R.REVIEW_SCORE),2) as SCORE
    from REST_INFO I
        join REST_REVIEW R
        on I.REST_ID = R.REST_ID
    where I.ADDRESS like '서울%'
    group by 1,2,3,4,5
    order by SCORE desc, I.FAVORITES desc