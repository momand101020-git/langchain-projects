#________STEPS___for_code_of _tools_________
#____1___install library_____
#____2__import_tools_____
#____3__object_create______
#____4__invoke() call____
#____5__result print______

from langchain_community.tools import DuckDuckGoSearchRun
tool=DuckDuckGoSearchRun()
result=tool.invoke("today news of pakistan")
print(result)

#______________________________________________________________________________________________
#______________________________________________________________________________________________


#______tool n0 2_____vikipedia___
#____install vikipedia___
# from langchain_community.tools import WikipediaQueryRun
# from langchain_community.utilities import WikipediaAPIWrapper

# #____it's helper to get data from wikipedia___and give to langchain___
# #)_____object form____
# api=WikipediaAPIWrapper()

# #______it's a tool____take user question___api use and return result_____
# tool=WikipediaQueryRun(api_wrapper=api)

# result=tool.invoke("python programming")
# print(result)


#__________________________________________________________________________________________________________
#__________________________________________________________________________________________________________


from langchain_experimental.tools import PythonREPLTool #_____experimental ka matlb hai ke feature abhi development_stage me hai
tool=PythonREPLTool()
result=tool.invoke('print(5+10)')
print(result)


#___________________________________________________________
#___________________________________________________________

#____human tool______
#________purposea___ ask the user foer input_________
from langchain_community.tools import HumanInputRun
human=HumanInputRun()
result=human.invoke("whats your name?")
print(result)



#______________________________________________________________________________ 
#______________________________________________________________________________


#___________________________stackExchangeTool_______________
#_________purpose___search programming questions____________

from langchain_community.tools import StackExchangeTool
tool=StackExchangeTool()
result=tool.invoke("how to make class and object in python")
print(result)