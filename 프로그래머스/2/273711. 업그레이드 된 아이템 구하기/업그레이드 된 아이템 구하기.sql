-- 코드를 작성해주세요
select ITEM_ID, ITEM_NAME, RARITY
    from ITEM_INFO 
    where ITEM_ID 
        in (select t.ITEM_ID
            from ITEM_TREE  t
                join ITEM_INFO i
                on t.PARENT_ITEM_ID = i.ITEM_ID
            where i.RARITY = "RARE")
    order by ITEM_ID desc
