from langchain.agents import create_agent
from src.langgraphagenticai.state.state import State


class ChatbotWithToolNode:

    def __init__(self, model):
        self.llm = model

    def create_chatbot(self, tools):

        agent = create_agent(
            model=self.llm,
            tools=tools
        )

        def chatbot(state):
            result = agent.invoke({"messages": state["messages"]})
            return {"messages": result["messages"]}

        return chatbot
    def process(self, state: State):

        messages = state["messages"]

        response = self.llm.invoke(messages)

        return {
        "messages": [response]
    }