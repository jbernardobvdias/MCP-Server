from fastmcp import FastMCP
from psycopg2.extras import RealDictCursor

from db.db import get_connection
from db.vector import get_embedding

tools = FastMCP("Knowledgebase Tools")

@tools.tool()
async def search_documents(query: str, top_k: int = 5) -> list[dict]:
    """Search the Entel knowledge base by semantic similarity."""
    embedding = get_embedding(query)
    conn = get_connection()
    try:
        with conn.cursor(cursor_factory=RealDictCursor) as cur:
            cur.execute("""
                SELECT doc_id, content, metadata,
                       1 - (embedding <=> %s) AS similarity
                FROM documents ORDER BY embedding <=> %s LIMIT %s;
            """, (embedding, embedding, top_k))
            return [dict(r) for r in cur.fetchall()]
    finally:
        conn.close()