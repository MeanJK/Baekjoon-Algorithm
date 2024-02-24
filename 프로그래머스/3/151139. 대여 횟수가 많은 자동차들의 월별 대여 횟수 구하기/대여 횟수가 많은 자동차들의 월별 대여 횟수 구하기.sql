WITH RECORDS(MONTH, CAR_ID) AS(
SELECT MONTH(START_DATE) AS MONTH, CAR_ID 
    FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
    WHERE DATE_FORMAT(START_DATE, '%Y-%m') BETWEEN '2022-08' AND '2022-10'
)

SELECT A.MONTH, A.CAR_ID, COUNT(*) AS RECORDS
FROM RECORDS A
WHERE (SELECT COUNT(*) FROM RECORDS B WHERE A.CAR_ID = B.CAR_ID) >= 5
GROUP BY A.CAR_ID, A.MONTH
ORDER BY A.MONTH, A.CAR_ID DESC