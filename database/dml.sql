
INSERT INTO users (username, email,hashed_password, is_active) VALUES
('Over', 'satoshinakamoto@gmail.com', '$2b$12$hashed_password_1', 1),
('pythonist', 'pitonist@gmail.com', '$2b$12$hashed_password_2', 1),
('ruster', 'rust22c@gmail.com', '$2b$12$hashed_password_3', 1),
('alice_dev', 'alice@example.com', '$2b$12$hashed_password_4', 1),
('bob_design', 'bob@example.com', '$2b$12$hashed_password_5', 1);



INSERT INTO posts (author_id, content, created_at) VALUES
(1, 'Hello everyone! This is my first post on this social network. Glad to be here!', '2025-11-09 17:40:00'),
(1, 'Today I learned SQLAlchemy and FastAPI. Great technologies for web development!', '2025-11-09 18:00:00'),
(2, 'Python is amazing! I love it for its simplicity and power.', '2025-11-09 17:50:00'),
(3, 'Rust is the language of the future! Memory safety and high performance.', '2025-11-09 18:05:00'),
(4, 'Im working on a new project with FastAPI. Who else is using it?', '2025-11-09 18:15:00'),
(5, 'Designers and developers must work together to create better products!', '2025-11-09 18:20:00'),
(1, 'Just finished setting up JWT authentication in my FastAPI app!', '2025-11-09 19:00:00');
