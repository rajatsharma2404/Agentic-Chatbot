from src.langgraphagenticai.state.state import State

class BasicChatBotNode:
    """
    Basic Chat Bot Node implementation
    """

    def __init__(self, model):
        self.llm=model

    def process(self, state: State) -> dict:
        """Process the input and generate an input"""
        response = self.llm.invoke(state["messages"])
        return {"messages": [response]}
