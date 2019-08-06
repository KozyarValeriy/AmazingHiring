SELECT 
    COUNT(DISTINCT email) as gmail
FROM 
    users 
WHERE email LIKE '%@gmail.com';
