select ID, EMAIL, FIRST_NAME, LAST_NAME
    from DEVELOPERS 
    where
        SKILL_CODE & (select CODE from SKILLCODES where NAME = 'Python')
        or
        SKILL_CODE & (select CODE from SKILLCODES where NAME = 'C#')        
    order by ID