-- Insert sample data
INSERT INTO articles (title, body, category) VALUES
('Intro to Databases', 'Database systems are used to store data efficiently.', 'database'),
('System Design', 'System design involves database architecture.', 'systems'),
('PostgreSQL Search', 'PostgreSQL supports full text search using GIN.', 'database');

-- Convert text to tsvector
UPDATE articles
SET doc = to_tsvector('english', body);

-- Search query
SELECT id, title
FROM articles
WHERE doc @@ to_tsquery('database');

-- Query execution plan
EXPLAIN ANALYZE
SELECT id, title
FROM articles
WHERE doc @@ to_tsquery('database');
