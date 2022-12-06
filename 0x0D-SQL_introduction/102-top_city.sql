-- script displaying top 3 cities temp during JULY and August by order of temp (descending)

SELECT city, AVG(value) AS avg_temp FROM temperatures WHERE month=7 OR month=8 GROUP BY city ORDER BY avg_temp DESC LIMIT 3;
