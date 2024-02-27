-- 코드를 작성해주세요
with front_end as (
    select sum(code)
    from SKILLCODES 
    where CATEGORY = "Front End"
)

select ID, EMAIL, FIRST_NAME, LAST_NAME
    from DEVELOPERS 
    where SKILL_CODE & (select * from front_end)
    order by id