from fastmcp import FastMCP
from fastmcp.prompts import Message
 
 
prompts = FastMCP("Maths Prompts")

@prompts.prompt()
async def solve_step_by_step(expression: str) -> list[Message]:
    """Prompt the LLM to solve a math expression step by step.
 
    Args:
        expression: The math expression to solve, e.g. '(4 + 5) * 2'.
    """
    return [
        Message(
            role="user",
            content=f"Solve the following expression step by step, showing your working: {expression}",
        )
    ]
 
@prompts.prompt()
async def explain_operation(operation: str) -> list[Message]:
    """Prompt the LLM to explain a math operation in simple terms.
 
    Args:
        operation: The operation to explain, e.g. 'division'.
    """
    return [
        Message(
            role="user",
            content=f"Explain the mathematical operation '{operation}' in simple terms with an example.",
        )
    ]
 