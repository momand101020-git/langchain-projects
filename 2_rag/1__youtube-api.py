from langchain_community.document_loaders import YoutubeLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_core.output_parsers import StrOutputParser
from langchain_community.vectorstores import FAISS
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
load_dotenv()
#_____toutube-transcript___________
url="https://www.youtube.com/watch?v=o126p1QN_RI"
loader=YoutubeLoader.from_youtube_url(
    url,
    add_video_info=False,
    language=["ur"]
)
docs=loader.load()
print(docs[0].page_content[:100])

#________________MAKE CHUNKS________________
splitter=RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200
)

chunk=splitter.split_documents(docs)
print("totall chunks:",len(chunk))
# print(chunk[0].page_content)


#____________embedding-model------------------
embeddings=HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-miniLM-L6-v2"
)
print("embedding ready")


#____________________________vector store me store___________________
vector_store=FAISS.from_documents(chunk, embeddings)
vector_store.save_local("youtube_faiss_db")
print("saved")

#_______________retriew_______
retriew=vector_store.as_retriever(
    search_type="similarity", 
    search_kwargs={"k":3}
)

#___llm___
llm = ChatGroq(model="llama-3.3-70b-versatile")
parser=StrOutputParser()


#____prompt___
prompt = PromptTemplate(
    input_variables=["context", "question"],
    template="""You are a helpful assistant.
Answer the question based on the context below.

If answer is not in context just say "I don't know".

Context: {context}

Question: {question}

Answer:"""
)

#_________________________question answer function__________
def ask(question):
    related_docs=retriew.invoke(question)
    context="\n\n ".join([d.page_content for d in related_docs])

    chain=prompt|llm|parser

    result=chain.invoke({
        "context":context,
        "question":question
    })

    return result
    

print("\n"+"="*50)
while True:
    question=input("enter your question ::")
    if question.lower()=="quite":
        print("byee")
        break
    answer=ask(question)
    print(f"answer is :::{answer}")
    print("-"*50)