
select i.ITEM_ID, i.ITEM_NAME, i.RARITY
    from ITEM_TREE t
        join (select ITEM_ID, ITEM_NAME, RARITY
            from ITEM_INFO   
            where RARITY = "RARE") r
        on t.PARENT_ITEM_ID = r.ITEM_ID
        join ITEM_INFO i
        on t.ITEM_ID = i.ITEM_ID
    order by i.ITEM_ID desc