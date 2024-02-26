-- 코드를 작성해주세요
# select *
#     from SKILLCODES 
select ID, EMAIL, FIRST_NAME, LAST_NAME
    from DEVELOPERS
    where
    (
        (length(bin(SKILL_CODE)) >= (select length(bin(CODE)) from SKILLCODES where NAME = 'Python'))
        and
        (left(right(cast(bin(SKILL_CODE) as char),(select length(bin(CODE)) from SKILLCODES where NAME = 'Python')),1)) = 1
    )
    or
    (
        (length(bin(SKILL_CODE)) >= (select length(bin(CODE)) from SKILLCODES where NAME = 'C#'))
        and
        (left(right(cast(bin(SKILL_CODE) as char),(select length(bin(CODE)) from SKILLCODES where NAME = 'C#')),1)) = 1
    )
    order by id

