-- script displaying average temp in farenheit by city ordered by temp descending

SELECT city, AVG(value) AS avg_temp FROM temperatures GROUP BY city ORDER BY avg_temp DESC;
