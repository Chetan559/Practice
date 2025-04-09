-- Write your PostgreSQL query statement below
SELECT u.name, COALESCE(SUM(r.distance),0) AS travelled_distance FROM Rides r
FULL OUTER JOIN Users u ON r.user_id = u.id
WHERE u.name IS NOT NULL
GROUP BY r.user_id, u.name
ORDER BY COALESCE(SUM(r.distance),0) DESC, u.name ASC;