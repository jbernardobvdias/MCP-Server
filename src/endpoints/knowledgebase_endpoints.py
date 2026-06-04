from fastmcp import FastMCP
from starlette.requests import Request
from starlette.responses import JSONResponse
import json

from db.db import get_connection
from db.vector import get_embedding

endpoints = FastMCP("Knowledgebase Endpoints")

@endpoints.custom_route("/kb/add", methods=["POST"])
async def add_to_kb(request: Request) -> JSONResponse:
    """
    Expected body:
    {
        "doc_id": "manual-hg8245h-v2",
        "content": "Full document text...",
        "metadata": { "category": "ONT", "model": "HG8245H" }
    }
    """
    body = await request.json()

    doc_id   = body.get("doc_id")
    content  = body.get("content")
    metadata = body.get("metadata", {})

    if not doc_id or not content:
        return JSONResponse({"error": "doc_id and content are required"}, status_code=400)

    embedding = get_embedding(content)

    conn = get_connection()
    try:
        with conn.cursor() as cur:
            cur.execute("""
                INSERT INTO documents (doc_id, content, metadata, embedding)
                VALUES (%s, %s, %s, %s)
                ON CONFLICT (doc_id) DO UPDATE
                    SET content   = EXCLUDED.content,
                        metadata  = EXCLUDED.metadata,
                        embedding = EXCLUDED.embedding;
            """, (doc_id, content, json.dumps(metadata), embedding))
        conn.commit()
        return JSONResponse({"status": "ok", "doc_id": doc_id})
    finally:
        conn.close()


@endpoints.custom_route("/kb/remove", methods=["POST"])
async def remove_from_kb(request: Request) -> JSONResponse:
    """
    Expected body: { "doc_id": "manual-hg8245h-v2" }
    """
    body = await request.json()
    doc_id = body.get("doc_id")

    if not doc_id:
        return JSONResponse({"error": "doc_id is required"}, status_code=400)

    conn = get_connection()
    try:
        with conn.cursor() as cur:
            cur.execute("DELETE FROM documents WHERE doc_id = %s;", (doc_id,))
            deleted = cur.rowcount
        conn.commit()
        return JSONResponse({
            "status": "ok" if deleted else "not_found",
            "doc_id": doc_id
        })
    finally:
        conn.close()
 