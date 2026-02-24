import streamlit as st
from langchain_core.messages import HumanMessage, AIMessage, ToolMessage
import json

class DisplayResultStreamlit:
    def __init__(self, usecase, graph, user_message):
        self.usecase=usecase
        self.graph=graph
        self.user_message=user_message

    def display_result_on_ui(self):

        if self.usecase == "Basic Chatbot":

            with st.chat_message("user"):
                st.write(self.user_message)

            for event in self.graph.stream({
                "messages": [HumanMessage(content=self.user_message)]
            }):

                for value in event.values():

                    if "messages" in value:
                        ai_reply = value["messages"][-1].content

                        with st.chat_message("assistant"):
                            st.write(ai_reply)
