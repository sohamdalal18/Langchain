import os
from dotenv import load_dotenv
load_dotenv()

# Setting Gemini API keys
os.environ['GEMINI_API_KEY'] = os.getenv("GEMINI_API_KEY")
#os.environ["GEMINI_PROJECT"] = os.getenv("GEMINI_PROJECT")
os.environ["LANGCHAIN_TRACING_V2"] = "true"

from langchain_google_genai import ChatGoogleGenerativeAI

# Initialize the Gemini LLM
llm = ChatGoogleGenerativeAI()  # Replace with the appropriate Gemini model
print(llm)

# Input and get response from the LLM
result = llm.invoke("What is generative AI?")
print(result)

# ChatPrompt Template
from langchain_core.prompts import ChatPromptTemplate

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are an expert AI Engineer. Provide me answers based on the questions"),
        ("user", "{input}")
    ]
)
print(prompt)

# Chain
chain = prompt | llm

response = chain.invoke({"input": "Can you tell me about Langsmith?"})
print(response)

# StrOutput Parser
from langchain_core.output_parsers import StrOutputParser
output_parser = StrOutputParser()

# Updated chain with output parser
chain = prompt | llm | output_parser

response = chain.invoke({"input": "Can you tell me about Langsmith?"})
print(response)
