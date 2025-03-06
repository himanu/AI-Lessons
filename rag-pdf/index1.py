import chromadb
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader
from uuid import uuid4
import os
from langchain_chroma import Chroma
from langchain import hub
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from langchain_cohere import ChatCohere
from langchain_core.messages import HumanMessage


local_path = "data/dark_matter.pdf"

# load the data
loader = PyPDFLoader("data/dark_matter.pdf")
pages = loader.load()

#split the data
text_splitter = RecursiveCharacterTextSplitter(chunk_size=7500, chunk_overlap=100)
chunks = text_splitter.split_documents(pages)
uuids = [str(uuid4()) for _ in range(len(chunks))]
results = [chunk.page_content for chunk in chunks]

# store the data
chroma_client = chromadb.Client()
collection = chroma_client.create_collection(name="my_collection")
collection.add(documents=results, ids=uuids)

# generate prompt
results = collection.query(
    query_texts=["in which year dark matter discovery was made?"], # Chroma will embed this for you
    n_results=4 # how many results to return
)
document = results['documents'][0][0]
print(document)

# llm model
# os.environ['COHERE_API_KEY'] = "1ffZglTZfhFR8XHpdnytW9pJ9HC74fPtJdTkubNC"
# llm = ChatCohere(model="command-r-plus")
# message = [HumanMessage(content="Hello, can you introduce yourself?")]
# print(llm.invoke(message).content)
# print((document))