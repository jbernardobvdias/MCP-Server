from fastmcp import FastMCP 

# from src.mcp.prompts.ex_prompts import prompts as ex_prompts

prompts = FastMCP("prompts")

# prompts.mount(ex_prompts)

__all__ = ["prompts"]
