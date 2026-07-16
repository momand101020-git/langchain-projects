from langchain_core.tools import tool
from langchain_core.messages import HumanMessage,ToolMessage
from langchain_groq import ChatGroq
from dotenv import load_dotenv
load_dotenv()

#__________create-tool__________
@tool
def multiply_num(a,b):
    """multiply the two numbers"""
    return a*b

#_________llm__________
llm=ChatGroq(model="llama-3.3-70b-versatile")



#__________bindtool____________________
llm_with_tool=llm.bind_tools([multiply_num])


#______________ask_question___________________tool-calling_________________________
response=llm_with_tool.invoke("multiplt 20 and 30")         #___print and see tool calls______
print(response.tool_calls[0]["args"])

# #_______________________execute-tool_______________________
tool_result=multiply_num.invoke(response.tool_calls[0]["args"])


# #________send tool result back to llm___________________
tool_message=ToolMessage(
    content=str(tool_result),
tool_call_id=response.tool_calls[0]["id"]
)



# #_______________final-answer__________________
final_response=llm_with_tool([
    HumanMessage(content='multiplt 20 and 30'),
    tool_message ,
    response
])
# print(final_responce.content)


#-----------------------------------------------------------
# chat-code
#-----------------------------------------------------------
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.tools import tool
from langchain_core.messages import HumanMessage, ToolMessage

load_dotenv()

# -----------------------------------
# Step 1: Create Tool
# -----------------------------------
@tool
def add(a: int, b: int) -> int:
    """Adds two numbers."""
    return a + b


# -----------------------------------
# Step 2: Create LLM
# -----------------------------------
llm = ChatGroq(
    model="llama-3.3-70b-versatile"
)

# -----------------------------------
# Step 3: Bind Tool with LLM
# -----------------------------------
llm_with_tools = llm.bind_tools([add])

# -----------------------------------
# Step 4: HumanMessage
# User asks a question
# -----------------------------------
messages = [
    HumanMessage(content="Add 20 and 30")
]

# -----------------------------------
# Step 5: AIMessage
# LLM decides to call the tool
# -----------------------------------
response = llm_with_tools.invoke(messages)

print("Tool Call:")
print(response.tool_calls)

# -----------------------------------
# Step 6: Execute Tool
# Run the Python function
# -----------------------------------
tool_result = add.invoke(response.tool_calls[0]["args"])

print("Tool Result:")
print(tool_result)

# -----------------------------------
# Step 7: ToolMessage
# Send tool result back to the LLM
# -----------------------------------
tool_message = ToolMessage(
    content=str(tool_result),
    tool_call_id=response.tool_calls[0]["id"]
)

# -----------------------------------
# Step 8: Final LLM Response
# Give complete conversation history
# -----------------------------------
final_response = llm_with_tools.invoke([
    HumanMessage(content="Add 20 and 30"),
    response,
    tool_message
])

print("Final Answer:")
print(final_response.content)


