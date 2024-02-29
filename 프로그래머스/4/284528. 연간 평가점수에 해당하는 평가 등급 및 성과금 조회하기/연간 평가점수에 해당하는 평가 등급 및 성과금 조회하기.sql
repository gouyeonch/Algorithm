-- 코드를 작성해주세요
with tbl as (select EMP_NO, 
    case when SUM(SCORE)/2 >= 96 then "S"
    when SUM(SCORE)/2 >= 90 then "A"
    when SUM(SCORE)/2 >= 80 then "B"
    else "C"
    end as GRADE,
    case when SUM(SCORE)/2 >= 96 then 20
    when SUM(SCORE)/2 >= 90 then 15
    when SUM(SCORE)/2 >= 80 then 10
    else 0
    end as BONUS
    from HR_GRADE 
    group by EMP_NO)
    
select e.EMP_NO, e.EMP_NAME, t.GRADE, e.SAL*t.BONUS/100 as BONUS
    from HR_EMPLOYEES e
        join tbl t
        on e.EMP_NO = t.EMP_NO
