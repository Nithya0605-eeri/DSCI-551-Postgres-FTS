import streamlit as st
import psycopg2
from psycopg2.extras import RealDictCursor

st.set_page_config(page_title="Article Search", layout="wide")

st.title("PostgreSQL Article Search")
st.write("Search articles using PostgreSQL full-text search with GIN indexing.")

DB_NAME = "articles_db"
DB_USER = "postgres"
DB_PASSWORD = "postgres"
DB_PORT = "5432"


def get_connection():
    hosts_to_try = ["127.0.0.1", "localhost", "host.docker.internal"]

    last_error = None
    for host in hosts_to_try:
        try:
            return psycopg2.connect(
                dbname=DB_NAME,
                user=DB_USER,
                password=DB_PASSWORD,
                host=host,
                port=DB_PORT,
            )
        except Exception as e:
            last_error = e

    raise last_error


query = st.text_input("Enter search keywords", placeholder="database")

if st.button("Search"):
    if query.strip():
        try:
            conn = get_connection()
            with conn.cursor(cursor_factory=RealDictCursor) as cur:
                cur.execute(
                    """
                    SELECT id, title
                    FROM articles
                    WHERE doc @@ plainto_tsquery('english', %s)
                    LIMIT 20;
                    """,
                    (query,),
                )
                rows = cur.fetchall()

            st.subheader("Results")

            if rows:
                for row in rows:
                    st.write(f"*ID:* {row['id']}")
                    st.write(f"*Title:* {row['title']}")
                    st.write("---")
            else:
                st.warning("No matching articles found.")

        except Exception as e:
            st.error(f"Database connection/query failed: {e}")
    else:
        st.warning("Please enter a keyword.")
