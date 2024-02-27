# 1230
with tbl as(select *, count(*) as CNT # 리뷰 제일 많이 작성한 리퓨 파싱
    from REST_REVIEW 
    group by MEMBER_ID
    order by CNT desc
    limit 1)

select p.MEMBER_NAME, r.REVIEW_TEXT, DATE_FORMAT(r.REVIEW_DATE, "%Y-%m-%d") as REVIEW_DATE
    from REST_REVIEW r
        join tbl t
        on r.MEMBER_ID = t.MEMBER_ID
        join MEMBER_PROFILE p
        on t.MEMBER_ID = p.MEMBER_ID
    order by REVIEW_DATE, r.REVIEW_TEXT