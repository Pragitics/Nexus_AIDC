

from google.adk.agents import Agent
from pydantic import BaseModel, Field
from google.adk.agents import LlmAgent


from google.adk.agents.llm_agent import Agent
from google.adk.tools.mcp_tool.mcp_toolset import MCPToolset,SseServerParams

root_agent = Agent(
    model="gemini-2.0-flash",
    name="finance_agent",
    instruction="""You are a finance agent for the Kite MCP platform.
1. When the user wants to log in, call the `login` tool to generate a URL.
2. Present this URL to the user. You MUST instruct them to complete the login and then to look at the URL in their browser's address bar AFTER they are successfully logged in.
3. You MUST tell them to find and copy the `request_token` value from that final URL and paste it back to you.
4. Once the user provides the request_token, you MUST call the `login` tool again, passing the token as an argument like this: `login(request_token='THE_USER_PROVIDED_TOKEN')`.
5. After this second call is successful, you can proceed with other actions like `get_holdings`.
6. Hey agent always use the same session to call the MCP Server.
""",
    description="This agent is used to interact with the MCP and provide financial information.",
    tools=[
        MCPToolset(
            connection_params=SseServerParams(
                url = 'https://mcp.kite.trade/sse'
            )
        )
    ],
)