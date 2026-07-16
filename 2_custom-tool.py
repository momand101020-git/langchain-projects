#______create custom tool____
#_____there are three steps to create costum tools_____
#_____now we make tool for multiplication that llm cannot do_____


#__step__1________make function fro your tool______

# def multiply(a,b):
#     """multiply two numbers"""   #__doc string
#     return a*b

#___step-2_________add type hints_____MEAN WHICH TYPE OF PAPRAMETERS ARE
# def multiply(a:int,b:int):
#     """multiply two numbers"""
#     return a*b

#____add tool decorator_______#tool____to make the function special___
# @tool
# def multiply(a,b):
#     """multiply two numbers"""
#     return a*b



#____________________HOW USE THIS TOOL NOW______________________
# from langchain_core.tools import tool
# @tool
# def multiply(a:int,b:int):
#     """multiply two numbers"""
#     return a*b

# result=multiply.invoke({"a":3,"b":5})
# print(result)

# print(multiply.name)                      #____ftn is special due to these steps
# print(multiply.description)
# print(multiply.args)


from langchain_core.tools import tool

@tool
def check_age(age:int):
    """check if a person is elligible based on age"""
    if age>50:
        return "not elliegible"
    else:
        return "elliegible"
    
result=check_age.invoke({"age":60})
print(result)

