with front_end as (
    select sum(CODE)
    from SKILLCODES 
    where CATEGORY = "Front End"
)

select 
    case when (SKILL_CODE & (select * from front_end))
        and (SKILL_CODE & (select CODE from SKILLCODES where NAME = "Python"))
        then "A"
        when (SKILL_CODE & (select CODE from SKILLCODES where NAME = "C#"))
        then "B"
        when (SKILL_CODE & (select * from front_end))
        then "C"
        end as GRADE
        ,ID, EMAIL
    from DEVELOPERS
    group by GRADE, ID, EMAIL
    having GRADE is not null
    order by GRADE, ID