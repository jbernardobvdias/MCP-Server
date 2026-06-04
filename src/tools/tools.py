from fastmcp import FastMCP 

from tools.knowledgebase_tools import tools as knowledgebase_tools
from tools.maths_tools import tools as maths_tools

tools = FastMCP("tools")

tools.mount(knowledgebase_tools)
tools.mount(maths_tools)

__all__ = ["tools"]
