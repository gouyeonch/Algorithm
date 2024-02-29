with tbl as (select EMP_NO, sum(SCORE) as SC
    from HR_GRADE 
    group by EMP_NO
    order by SC desc
    limit 1)
    
select t.SC as SCORE, e.EMP_NO, EMP_NAME, POSITION, EMAIL
    from HR_EMPLOYEES e
        join tbl t
        on e.EMP_NO = t.EMP_NO
    