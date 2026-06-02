from fastmcp import FastMCP 

from src.tools.maths_tools import tools as maths_tools

tools = FastMCP("tools")

tools.mount(maths_tools)

__all__ = ["tools"]
