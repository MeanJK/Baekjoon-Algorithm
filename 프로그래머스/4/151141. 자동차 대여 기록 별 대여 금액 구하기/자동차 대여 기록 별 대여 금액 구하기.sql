WITH RENTAL_HISTORY AS (
    SELECT *,
        CASE
            WHEN (DATEDIFF(END_DATE, START_DATE) + 1 < 7) THEN NULL
            WHEN (DATEDIFF(END_DATE, START_DATE) + 1 < 30) THEN '7일 이상'
            WHEN (DATEDIFF(END_DATE, START_DATE) + 1 < 90) THEN '30일 이상'
            ELSE '90일 이상'
            END AS DURATION_TYPE
        FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY)
,
TRUCKS AS(
SELECT * FROM CAR_RENTAL_COMPANY_CAR
WHERE CAR_TYPE = '트럭')

SELECT R.HISTORY_ID, IF (R.DURATION_TYPE IS NULL,
                        (DATEDIFF(END_DATE, START_DATE)+1) * T.DAILY_FEE,
                        ROUND((DATEDIFF(END_DATE, START_DATE)+1) *(T.DAILY_FEE * (1-P.DISCOUNT_RATE / 100))))
                        AS FEE
FROM TRUCKS T INNER JOIN RENTAL_HISTORY R ON R.CAR_ID = T.CAR_ID LEFT JOIN CAR_RENTAL_COMPANY_DISCOUNT_PLAN P ON T.CAR_TYPE = P.CAR_TYPE AND R.DURATION_TYPE = P.DURATION_TYPE
GROUP BY R.HISTORY_ID
ORDER BY FEE DESC, R.HISTORY_ID DESC