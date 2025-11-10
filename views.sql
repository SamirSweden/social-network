CREATE VIEW  post_details AS
SELECT
    p.id,
    p.content,
    p.created_at,
    p.author_id ,
    u.username as author_username,
    u.email as author_email,
    u.is_active as author_active,
    u.created_at as author_created_at
FROM posts p
JOIN users u ON p.author_id = u.id
WHERE u.is_active = TRUE;


CREATE VIEW  user_stats AS
SELECT
    u.id,
    u.username,
    u.email ,
    u.is_active,
    u.created_at,
    COUNT(p.id) as last_post_date
FROM users u
LEFT JOIN posts ON u.id = p.author_id
GROUP BY u.id, u.username, u.email,u.is_active,u.created_at
