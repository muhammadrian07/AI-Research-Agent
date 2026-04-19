import os
import random

from dotenv import load_dotenv
from pydantic import BaseModel
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import PydanticOutputParser
from langchain_core.messages import HumanMessage, SystemMessage, ToolMessage
from tools import search_tool, wikipedia_tool, wikipedia_detailed_tool

load_dotenv(override=True)


class ResearchResponse(BaseModel):
    topic: str
    summary: str
    sources: list[str]
    tools_used: list[str]


gemini_api_key = os.getenv("GEMINI_API_KEY")
if not gemini_api_key:
    raise RuntimeError("Missing GEMINI_API_KEY in .env")

model_name = random.choice(["gemini-2.5-flash", "gemini-2.5-flash-lite"])
llm = ChatGoogleGenerativeAI(model=model_name, google_api_key=gemini_api_key)

parser = PydanticOutputParser(pydantic_object=ResearchResponse)

llm_with_tools = llm.bind_tools([search_tool, wikipedia_tool, wikipedia_detailed_tool])

system_prompt = (
    "You are a research assistant that will help generate a research paper. "
    "Answer the user query using necessary tools and information. "
    "Wrap the output in this format and provide no other text\n"
    + parser.get_format_instructions()
)

user_query = input("What can I help you research? ")

messages = [
    SystemMessage(content=system_prompt),
    HumanMessage(content=user_query),
]

# Agentic loop — keep going until the model stops calling tools
while True:
    response = llm_with_tools.invoke(messages)
    messages.append(response)

    # If no tool calls, we have the final answer
    if not response.tool_calls:
        break

    # Execute each tool call and feed results back
    for tool_call in response.tool_calls:
        print(f"Calling tool: {tool_call['name']} with input: {tool_call['args']}")
        
        # Route to correct tool
        if tool_call['name'] == 'search':
            tool_result = search_tool.invoke(tool_call["args"])
        elif tool_call['name'] == 'wikipedia':
            tool_result = wikipedia_tool.invoke(tool_call["args"])
        elif tool_call['name'] == 'wikipedia_detailed':
            tool_result = wikipedia_detailed_tool.invoke(tool_call["args"])
        else:
            tool_result = "Tool not found"
        
        messages.append(
            ToolMessage(content=str(tool_result), tool_call_id=tool_call["id"])
        )

output = response.content

try:
    structured_response = parser.parse(output)
    print(structured_response)
except Exception as e:
    print("Error parsing structured response:", e)
    print("Raw output:", output)