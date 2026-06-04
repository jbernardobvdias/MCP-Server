# FastMCP Server
 
A learning project for building MCP (Model Context Protocol) servers with [FastMCP](https://gofastmcp.com), PostgreSQL, and Docker.
 
## Stack
 
- **[FastMCP](https://gofastmcp.com)** — MCP server framework
- **PostgreSQL + pgvector** — database with vector support
- **Docker Compose** — local development environment
- **Pydantic Settings** — environment-based configuration
- **Loguru** — structured logging
 
## Getting Started
 
**1. Clone and configure**
 
```bash
git clone https://github.com/jbernardobvdias/{project}.git
cd {project}
```
 
**2. Fill in your `.env`**
 
```env
TRANSPORT=http
HOST=0.0.0.0
PORT=8000
SERVER_NAME=FastMCP-Server
SERVER_INSTRUCTIONS=FastMCP Server

DB_POSTGRES_USER=
DB_POSTGRES_PASSWORD=
DB_POSTGRES_DB=
DB_POSTGRES_HOST=
DB_POSTGRES_PORT=5432

OPENAI_KEY=sk-**************
EMBEDDINGS_MODEL=text-embedding-3-small
```
 
**3. Run with Docker**
 
```bash
docker compose up --build
```
 
**4. Test it**
 
```bash
curl http://localhost:8000/health
```
  
## Running Locally (without Docker)
 
```bash
pip install -r requirements.txt
python src/main.py
```