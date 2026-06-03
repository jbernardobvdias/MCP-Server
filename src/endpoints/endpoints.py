from fastmcp import FastMCP 

from endpoints.base_endpoints import endpoints as base_endpoints

endpoints = FastMCP("endpoints")

endpoints.mount(base_endpoints)

__all__ = ["endpoints"]