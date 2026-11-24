from mcp.server import MCPServer

mcp = MCPServer(
    "Student Utility Server",
    instructions="MCP server for student utilities and calculations."
)


@mcp.tool()
def add_numbers(a: int, b: int) -> int:
    """Add two numbers."""
    return a + b


@mcp.tool()
def calculate_average(
    mark1: float,
    mark2: float,
    mark3: float
) -> float:
    """Calculate the average of three student marks."""
    return round((mark1 + mark2 + mark3) / 3, 2)


@mcp.resource("student://profile")
def student_profile() -> str:
    """Return student information."""

    return """
    Student Name: Anu
    Subject: Artificial Intelligence
    Marks: 85, 90, 95
    """


@mcp.prompt()
def explain_mcp(topic: str) -> str:
    """Generate an educational prompt about MCP."""

    return f"Explain {topic} in simple language with an example."


if __name__ == "__main__":
    print("Starting MCP Server...", flush=True)

    mcp.run(
        transport="streamable-http",
        host="127.0.0.1",
        port=8000
    )