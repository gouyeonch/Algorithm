-- 코드를 입력하세요
SELECT ANIMAL_TYPE, 
    if(NAME is NULL, "No name", NAME) as NAME, SEX_UPON_INTAKE
    from ANIMAL_INS 
    order by ANIMAL_ID