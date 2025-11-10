
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT ,
    username VARCHAR(50) UNIQUE NOT NULL ,
    email VARCHAR(100) UNIQUE NOT NULL ,
    hashed_password TEXT NOT NULL ,
    is_active BOOLEAN DEFAULT TRUE ,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);


CREATE TABLE IF NOT EXISTS posts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    author_id INTEGER NOT NULL,
    content TEXT NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP ,
    FOREIGN KEY (author_id) REFERENCES users(id) ON DELETE CASCADE
);


CREATE INDEX IF NOT EXISTS idx_users_username ON users(username);
CREATE INDEX IF NOT EXISTS idx_users_email ON users(email);
CREATE INDEX IF NOT EXISTS idx_posts_author_id ON posts(author_id);
CREATE INDEX IF NOT EXISTS idx_posts_created_at ON posts(created_at);

CREATE UNIQUE INDEX  IF NOT EXISTS uq_users_username ON users(username);
CREATE UNIQUE INDEX  IF NOT EXISTS uq_users_email ON users(email);





