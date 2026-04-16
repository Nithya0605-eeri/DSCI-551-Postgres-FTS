CREATE TABLE articles (
    id SERIAL PRIMARY KEY,
    title TEXT,
    body TEXT,
    category TEXT,
    published_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    doc tsvector
);

CREATE INDEX idx_articles_doc
ON articles USING GIN(doc);