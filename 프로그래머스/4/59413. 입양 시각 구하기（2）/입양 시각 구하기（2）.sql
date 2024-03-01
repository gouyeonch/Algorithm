# -- 코드를 입력하세요
SET @HOUR = -1;
select (@HOUR := @HOUR + 1) HOUR, 
    (select COUNT(HOUR(DATETIME))
        from ANIMAL_OUTS
        where (HOUR(DATETIME) = @HOUR)) as COUNT
    from ANIMAL_OUTS 
    where @HOUR < 23
    group by HOUR
# select *,HOUR(DATETIME) as HOUR, COUNT(*)
#     from ANIMAL_OUTS
#     group by HOUR