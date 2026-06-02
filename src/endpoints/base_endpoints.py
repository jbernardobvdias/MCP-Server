from fastmcp import FastMCP
from starlette.requests import Request
from starlette.responses import JSONResponse
 
endpoints = FastMCP("Base Endpoints")
 
 
@endpoints.custom_route("/health", methods=["GET"])
async def health(request: Request) -> JSONResponse:
    return JSONResponse({"status": "ok"})
 
 
@endpoints.custom_route("/echo", methods=["POST"])
async def echo(request: Request) -> JSONResponse:
    body = await request.json()
    return JSONResponse(body)
 