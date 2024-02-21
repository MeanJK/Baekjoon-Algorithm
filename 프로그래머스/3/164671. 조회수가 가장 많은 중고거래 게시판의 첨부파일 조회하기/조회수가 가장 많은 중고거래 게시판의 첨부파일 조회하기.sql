SELECT CONCAT('/',CONCAT_WS('/',
                 'home',
                 'grep',
                 'src',
                 B.BOARD_ID,
                 F.FILE_ID),
                 F.FILE_NAME,
                 F.FILE_EXT) AS FILE_PATH
FROM USED_GOODS_BOARD B JOIN USED_GOODS_FILE F ON B.BOARD_ID = F.BOARD_ID
WHERE B.BOARD_ID IN (SELECT BOARD_ID FROM
                     (SELECT *, DENSE_RANK() OVER (ORDER BY VIEWS DESC) AS VIEW_RANK
                     FROM USED_GOODS_BOARD)
                     INLINE
                     WHERE VIEW_RANK = 1
                    )
ORDER BY F.FILE_ID DESC