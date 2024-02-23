select i.ITEM_ID, i.ITEM_NAME, i.RARITY
    from ITEM_TREE t
        right join ITEM_INFO i
        on t.PARENT_ITEM_ID = i.ITEM_ID
    where t.ITEM_ID is null
    order by i.ITEM_ID desc