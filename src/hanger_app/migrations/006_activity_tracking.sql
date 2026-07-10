ALTER TABLE users ADD COLUMN last_login_at INTEGER;

CREATE INDEX IF NOT EXISTS idx_users_last_login_at
ON users(last_login_at);
