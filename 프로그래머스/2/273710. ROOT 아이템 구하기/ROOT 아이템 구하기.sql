-- 코드를 작성해주세요
select t.ITEM_ID, i.ITEM_NAME
    from ITEM_TREE t
        join ITEM_INFO i
        on t.ITEM_ID = i.ITEM_ID
    where PARENT_ITEM_ID is NULL
    order by t.ITEM_ID