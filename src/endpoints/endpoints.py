from fastmcp import FastMCP 

from endpoints.base_endpoints import endpoints as base_endpoints
from endpoints.knowledgebase_endpoints import endpoints as knowledgebase_endpoints

endpoints = FastMCP("endpoints")

endpoints.mount(base_endpoints)
endpoints.mount(knowledgebase_endpoints)

__all__ = ["endpoints"]