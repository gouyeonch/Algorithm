-- 코드를 입력하세요
SELECT F.FLAVOR
    from FIRST_HALF F
        join ICECREAM_INFO I
        on F.FLAVOR = I.FLAVOR
    where TOTAL_ORDER  > 3000 and I.INGREDIENT_TYPE = 'fruit_based'