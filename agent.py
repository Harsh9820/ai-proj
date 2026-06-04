import os

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()

llm = ChatOpenAI(
    model="openai/gpt-oss-120b:free",
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("API_KEY")
)

def chatbot_node(state):
    question = state["question"]

    response = llm.invoke(question)

    return {
        "answer": response.content
    }

def researcher_node(state):

    question = state["question"]

    response = llm.invoke(
        f"Research this topic: {question}"
    )

    return {
        "research": response.content
    }

def writer_node(state):

    research = state["research"]

    response = llm.invoke(
        f"Write a clean answer using:\n{research}"
    )

    return {
        "answer": response.content
    }