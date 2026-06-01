from src.settings import settings

from fastmcp import FastMCP
from loguru import logger

from src.mcp.endpoints.endpoints import endpoints
from src.mcp.prompts.prompts import prompts
from src.mcp.resources.resources import resources
from src.mcp.tools.tools import tools

def main():
    mcp = FastMCP(
        name=settings.server_name,
        instructions=settings.server_instructions,
    )

    mcp.mount(endpoints)
    mcp.mount(tools)
    mcp.mount(resources)
    mcp.mount(prompts)

    logger.info("MCP server configured successfully, starting...")

    mcp.run(
        transport=settings.transport,
        host=settings.host,
        port=settings.port,
    )


if __name__ == "__main__":
    main()