from src.langgraphagenticai.state.state import State

class BasicChatBotNode:

    def __init__(self, model):
        self.llm = model

    def process(self, state: State):

        messages = state["messages"]

        response = self.llm.invoke(messages)

        return {
            "messages": [response]
        }
    
    def create_chatbot(self, tools):
        """
        returns chatbot node function
        """
        llm_with_tools = self.llm.bind_tools(tools)

        def chatbot_node(state: State):
            """
            Chatbot logic for processing the input state and returning a response
            """
            return {"messages": [llm_with_tools.invoke(state["messages"])]}
        
        return chatbot_node
