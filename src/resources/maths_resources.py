from fastmcp import FastMCP
 
resources = FastMCP("Maths Resources")

@resources.resource("math://operations")
async def get_operations() -> dict:
    """Returns the available math operations and their descriptions."""
    return {
        "operations": [
            {"name": "add_numbers", "description": "Add two numbers together"},
            {"name": "subtract_numbers", "description": "Subtract one number from another"},
            {"name": "multiply_numbers", "description": "Multiply two numbers together"},
            {"name": "divide_numbers", "description": "Divide one number by another"},
        ]
    }
 
@resources.resource("math://constants")
async def get_constants() -> dict:
    """Returns common mathematical constants."""
    return {
        "constants": [
            {"name": "pi", "value": 3.141592653589793, "description": "Ratio of a circle's circumference to its diameter"},
            {"name": "e", "value": 2.718281828459045, "description": "Base of the natural logarithm"},
            {"name": "phi", "value": 1.618033988749895, "description": "The golden ratio"},
        ]
    }
