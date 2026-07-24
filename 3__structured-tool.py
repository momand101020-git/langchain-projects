# from langchain_core.tools import StructuredTool
# from pydantic import BaseModel, Field



# #____from noraml function_____
# def mult_func(a,b):
#     return a*b

# #____make pydantic class____blueprint for llm____ 
# #___input schema________
# class multiply_input(BaseModel):
#     a:int=Field(description="the first number to add")
#     b:int=Field(description="the second number to add")

#_____________convert function into structured tool__________
# multiply_tool=StructuredTool.from_function(
#     func=mult_func,
#     name="multiply",
#     description="multiply two numbers",
#     args_schema=multiply_input
# )


# result=multiply_tool.invoke({"a":4,"b":6}) 
# print(result)


#____________________________________________________
from langchain_core.tools import StructuredTool
from pydantic import BaseModel,Field

def add(a,b):
    return a+b

class add_num(BaseModel):
    a:int=Field(description="first number to add")
    b:int=Field(description="second number to add")

tool =StructuredTool.from_function(
    func=add,
    name="addition",
    description="add the two numbers",
    args_schema=add_num
)

result=tool.invoke({"a":100,"b":100})
print(result)



#_______________example_________________
def check_age(age):
    if age>50:
        return "you are not elligible"
    else:
        return "you are elligible"
    
class ageinput(BaseModel):
    age:int=Field(description="calcukate the age")

tool=StructuredTool.from_function(
    func=check_age,
    name="check_age",
    description="check whether a person is elligible based on age",
    args_schema=ageinput
)

result=tool.invoke({"age":40})
print(result)
