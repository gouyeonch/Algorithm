-- 코드를 입력하세요
SELECT CONCAT("/home/grep/src/",b.BOARD_ID,"/",FILE_ID,FILE_NAME,FILE_EXT) as FILE_PATH
    from USED_GOODS_BOARD b
        join USED_GOODS_FILE f
        on b.BOARD_ID = f.BOARD_ID
    where b.VIEWS =
        (select MAX(VIEWS)
            from USED_GOODS_BOARD)
    order by f.FILE_ID desc