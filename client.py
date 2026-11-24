import asyncio
from mcp import Client


async def main():

    print("Connecting to MCP Server...")

    async with Client("http://127.0.0.1:8000/mcp") as client:

        print("\nConnected Successfully!")

        # Server Information
        print("\n===== SERVER INFORMATION =====")
        print("Server:", client.server_info.name)

        # List Available Tools
        print("\n===== AVAILABLE TOOLS =====")

        tools = await client.list_tools()

        for tool in tools.tools:
            print("Tool:", tool.name)
            print("Description:", tool.description)

        # Addition Tool
        print("\n===== ADDITION TOOL =====")

        result = await client.call_tool(
            "add_numbers",
            {"a": 20, "b": 30}
        )

        print("Addition Result:", result.content)

        # Average Tool
        print("\n===== AVERAGE TOOL =====")

        result = await client.call_tool(
            "calculate_average",
            {
                "mark1": 80,
                "mark2": 90,
                "mark3": 100
            }
        )

        print("Average Result:", result.content)

        # Read Student Resource
        print("\n===== STUDENT RESOURCE =====")

        resource = await client.read_resource(
            "student://profile"
        )

        for item in resource.contents:
            print(item)

        # List Prompts
        print("\n===== AVAILABLE PROMPTS =====")

        prompts = await client.list_prompts()

        for prompt in prompts.prompts:
            print("Prompt:", prompt.name)

        # Get Prompt
        print("\n===== MCP PROMPT =====")

        prompt_result = await client.get_prompt(
            "explain_mcp",
            {"topic": "Model Context Protocol"}
        )

        for message in prompt_result.messages:
            print(message.content)

        print("\n===== EXECUTION COMPLETED =====")


if __name__ == "__main__":
    asyncio.run(main())