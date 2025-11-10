SELECT
    p.id as post_id,
    p.content,
    p.created_at as post_created,
    u.username as author,
    u.created_at as author_joined
FROM posts p
JOIN users u ON p.author = u.id
WHERE u.username = 'Over'
ORDER BY p.created_at DESC;


SELECT
    p.id,
    p.content,
    p.created_at,
    u.username,
    u.created_at
FROM posts p
JOIN users u ON p.author_id = u.id
WHERE u.is_active = TRUE
ORDER BY p.created_at DESC
LIMIT 5;


SELECT
    u.username ,
    COUNT(p.id) as total_posts,
    MIN(p.created_at) as first_post,
    MAX(p.created_at) AS last_post
FROM users u
LEFT JOIN posts p ON u.id = p.author_id
GROUP BY u.id , u.username
ORDER BY total_posts DESC;


SELECT
    p.id,
    p.content,
    p.created_at,
    u.username
FROM posts p
JOIN users u ON p.author_id = u.id
WHERE p.content LIKE '%FastAPI%' OR p.content LIKE '%Python%'
ORDER BY p.created_at DESC;






