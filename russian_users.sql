SELECT
	users.id,
	users.first_name,
	users.last_name,
	users.email,
    counties.name AS country
FROM users, cities, counties
WHERE users.city_id = cities.id 
	AND cities.country_id = counties.id 
	AND counties.name = 'Russia'
ORDER BY users.id;