import os
import psycopg2
from fastmcp import FastMCP

from pgvector.psycopg2 import register_vector

endpoints = FastMCP("Knowledgebase Endpoints")

# Run once
def init_db():
    conn = get_connection()
    with conn.cursor() as cur:
        cur.execute("CREATE EXTENSION IF NOT EXISTS vector;")
        cur.execute("""
            CREATE TABLE IF NOT EXISTS documents (
                id          SERIAL PRIMARY KEY,
                doc_id      TEXT UNIQUE NOT NULL,
                content     TEXT NOT NULL,
                metadata    JSONB,
                embedding   vector(1536)   -- match your model's dimensions
            );
        """)
        cur.execute("""
            CREATE INDEX IF NOT EXISTS documents_embedding_idx
            ON documents USING ivfflat (embedding vector_cosine_ops)
            WITH (lists = 100);
        """)
        conn.commit()
    conn.close()

def get_connection():
    conn = psycopg2.connect(os.environ["DATABASE_URL"])
    register_vector(conn)
    return conn

