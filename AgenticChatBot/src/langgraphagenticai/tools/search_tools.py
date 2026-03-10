from langchain_community.tools.tavily_search import TavilySearchResults
from langgraph.prebuilt import ToolNode


def get_tools(tavily_api_key=None):

    tools = []

    if tavily_api_key:
        tavily_tool = TavilySearchResults(
            max_results=3,
            tavily_api_key=tavily_api_key
        )

        # Explicitly define tool metadata required by Groq
        tavily_tool.name = "tavily_search"
        tavily_tool.description = "Search the web for latest information and news"

        tools.append(tavily_tool)

    return tools


def create_tool_node(tools):
    return ToolNode(tools=tools)