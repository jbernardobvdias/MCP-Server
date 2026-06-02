from fastmcp import FastMCP

tools = FastMCP("Maths Tools")

@tools.tool()
async def add_numbers(a: float, b: float) -> float:
    """Add two numbers together.
 
    Args:
        a: First number to add.
        b: Second number to add.
 
    Returns:
        float: The sum of a and b.
    """
    return a + b
 
@tools.tool()
async def subtract_numbers(a: float, b: float) -> float:
    """Subtract one number from another.
 
    Args:
        a: The number to subtract from.
        b: The number to subtract.
 
    Returns:
        float: The difference of a and b.
    """
    return a - b
 
@tools.tool()
async def multiply_numbers(a: float, b: float) -> float:
    """Multiply two numbers together.
 
    Args:
        a: First number to multiply.
        b: Second number to multiply.
 
    Returns:
        float: The product of a and b.
    """
    return a * b

@tools.tool()
async def divide_numbers(a: float, b: float) -> float:
    """Divide one number by another.
 
    Args:
        a: The dividend (number to be divided).
        b: The divisor (number to divide by).
 
    Returns:
        float: The quotient of a divided by b.
 
    Raises:
        ValueError: If b is zero.
    """
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b