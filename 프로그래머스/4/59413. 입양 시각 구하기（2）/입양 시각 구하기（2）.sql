-- 코드를 입력하세요
SET @hour = -1;
SELECT (@hour := @hour + 1) "HOUR",
    (select count(DATETIME)
        from ANIMAL_OUTS 
        where hour(DATETIME) = @hour) "COUNT"
    from ANIMAL_OUTS
    where @HOUR < 23
    order by @HOUR