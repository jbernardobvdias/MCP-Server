from fastmcp import FastMCP 

# from src.mcp.resources.ex_resources import resources as ex_resources

resources = FastMCP("resources")

# resources.mount(ex_resources)

__all__ = ["resources"]
