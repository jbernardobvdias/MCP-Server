from fastmcp import FastMCP 

from resources.maths_resources import resources as maths_resources

resources = FastMCP("resources")

resources.mount(maths_resources)

__all__ = ["resources"]
