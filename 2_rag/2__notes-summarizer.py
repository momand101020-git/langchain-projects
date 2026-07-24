from langchain_community.document_loaders import PyPDFLoader
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
load_dotenv() 



#__________load pdf____________
loader=PyPDFLoader("2__RAG-BASE-SYSTEM\pdf_practice.pdf")

docs=loader.load()

print(docs[0].page_content[:300])


#____________splitter_____________________

splitter=RecursiveCharacterTextSplitter(
    chunk_size=1000,
    # chunK_overlap=200
)
 
chunk=splitter.split_documents(docs)
print(len(chunk))
print(chunk[0].page_content)


llm=ChatGroq(model="llama-3.3-70b-versatile")

parser=StrOutputParser()


#_______________prompt_______
temp= PromptTemplate(
    template="""you are an expert notes summarizer.
    summarize the following text in simple english.
    text: {text}"""
)

chain = temp|llm|parser 

full_text="\n\n".join([chunks.page_content for chunks in chunk])

summary=chain.invoke({"text":full_text})

print("-"*50)

print("summary :",summary)
