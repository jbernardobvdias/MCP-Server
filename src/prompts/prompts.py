from fastmcp import FastMCP 

from prompts.maths_prompts import prompts as maths_prompts

prompts = FastMCP("prompts")

prompts.mount(maths_prompts)

__all__ = ["prompts"]
