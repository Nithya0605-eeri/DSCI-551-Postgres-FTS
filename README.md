# PostgreSQL Full-Text Search with GIN Indexing

## Project Overview
This project implements a lightweight article search system using PostgreSQL’s full-text search functionality. It demonstrates how database internals such as tsvector, tsquery, and GIN indexing improve search performance.

---

## Setup Instructions

### 1. Start PostgreSQL (Docker)
docker start dsci551-postgres

### 2. Connect to Database
docker exec -it dsci551-postgres psql -U postgres -d articles_db

### 3. Run Schema
\i schema/schema.sql

### 4. Insert Sample Data
INSERT INTO articles (title, body, category) VALUES
('Intro to Databases', 'Database systems are used to store data efficiently.', 'database'),
('System Design', 'System design involves database architecture.', 'systems'),
('PostgreSQL Search', 'PostgreSQL supports full text search using GIN.', 'database');

### 5. Convert Text to Searchable Format
UPDATE articles
SET doc = to_tsvector('english', body);

---

## Search Query

SELECT id, title
FROM articles
WHERE doc @@ to_tsquery('database');

---

## Query Execution Analysis

EXPLAIN ANALYZE
SELECT id, title
FROM articles
WHERE doc @@ to_tsquery('database');

---

## Features

- Full-text search using tsvector and tsquery
- GIN index for efficient keyword search
- Query performance analysis using EXPLAIN ANALYZE

---

## Repository Structure

schema/ → table + index  
queries/ → sample queries  
README.md → setup instructions  

---

## Conclusion

This project demonstrates how PostgreSQL’s internal indexing mechanisms significantly improve search performance in text-based applications.
# PostgreSQL Full-Text Search Project

## Setup

1. Start PostgreSQL:
docker start dsci551-postgres

2. Connect:
docker exec -it dsci551-postgres psql -U postgres -d articles_db

3. Run schema:
\i schema/schema.sql

## Features
- Full-text search using tsvector and tsquery
- GIN index
- EXPLAIN ANALYZE performance analysis
# PostgreSQL Full-Text Search with GIN Indexing

This project demonstrates a lightweight article search system using PostgreSQL full-text search, tsvector, tsquery, and GIN indexing.

## Project Overview

The goal of this project is to improve search performance on text data by using PostgreSQL full-text search instead of scanning every row.

## Features

- Full-text search using tsvector and tsquery
- GIN index for faster keyword lookup
- EXPLAIN ANALYZE for query plan inspection
- Simple Streamlit app for article search

## Setup Instructions

### 1. Start PostgreSQL
```bash
docker start dsci551-postgres# PostgreSQL Full-Text Search with GIN Indexing

This project demonstrates a lightweight article search system using PostgreSQL full-text search, tsvector, tsquery, and GIN indexing.

## Project Overview

The goal of this project is to improve search performance on text data by using PostgreSQL full-text search instead of scanning every row.

## Features

- Full-text search using tsvector and tsquery
- GIN index for faster keyword lookup
- EXPLAIN ANALYZE for query plan inspection
- Simple Streamlit app for article search

## Setup Instructions

### 1. Start PostgreSQL
```bash
docker start dsci551-postgres