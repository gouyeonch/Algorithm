with TBL as (select MEMBER_ID, count(MEMBER_ID) as cc
    from REST_REVIEW 
    group by MEMBER_ID
    order by cc desc
    limit 1)

select MEMBER_NAME, REVIEW_TEXT, DATE_FORMAT(REVIEW_DATE, "%Y-%m-%d") as REVIEW_DATE
    from REST_REVIEW r
        join MEMBER_PROFILE p
        on r.MEMBER_ID = p.MEMBER_ID
        join TBL t
        on r.MEMBER_ID = t.MEMBER_ID
    order by REVIEW_DATE, REVIEW_TEXT