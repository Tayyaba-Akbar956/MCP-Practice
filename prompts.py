from mcp.server.fastmcp import FastMCP


mcp = FastMCP("Demo Server",stateless_http = True)

@mcp.prompt("Add")
def add_two_numbers() -> int:
    return "Add all the given numbers and return the result."

@mcp.prompt("Github Profile")
def get_github_profile(username: str) -> str:
    return f"Fetch the github profile information for the username: {username} and summarize the details."

app = mcp.streamable_http_app()