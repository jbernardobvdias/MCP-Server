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
MCP_TRANSPORT=http
MCP_HOST=0.0.0.0
MCP_PORT=8000
MCP_SERVER_NAME=FastMCP-Server
MCP_SERVER_INSTRUCTIONS=FastMCP Server

MCP_DB_ENABLED=false
MCP_DB_POSTGRES_USER=
MCP_DB_POSTGRES_PASSWORD=
MCP_DB_POSTGRES_DB=
MCP_DB_POSTGRES_HOST=
MCP_DB_POSTGRES_PORT=5432
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
python main.py
```