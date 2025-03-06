import langchain
from langchain_community.document_loaders import PyPDFLoader
import os
import getpass
from langchain_chroma import Chroma
from langchain_cohere.embeddings import CohereEmbeddings
from uuid import uuid4
import ssl

# try:
#     _create_unverified_https_context = ssl._create_unverified_context
# except AttributeError:
#     # Legacy Python that doesn't verify HTTPS certificates by default
#     pass
# else:
#     # Handle target environment that doesn't support HTTPS verification
#     print("himanshu yadav")
#     ssl._create_default_https_context = _create_unverified_https_context

# load the data
loader = PyPDFLoader("data/dark_matter.pdf")
# split the data
pages = loader.load_and_split()


# store the data in vector store
## prompt user for open ai api key
# 1ffZglTZfhFR8XHpdnytW9pJ9HC74fPtJdTkubNC
os.environ['COHERE_API_KEY'] = "1ffZglTZfhFR8XHpdnytW9pJ9HC74fPtJdTkubNC"

# embedding
embeddings = CohereEmbeddings(model="embed-english-light-v3.0")

## load pages in vector store and use cohere embeddings
db = Chroma(
    collection_name="example_collection",
    embedding_function=embeddings,
    persist_directory="./chroma_langchain_db",  # Where to save data locally, remove if not neccesary
)


uuids = [str(uuid4()) for _ in range(len(pages))]
db.add_documents(documents=pages, ids = uuids)
# db = Chroma.from_documents(pages, embeddings)
# a function that accept query text
def my_function(query):
  print("Hello from a function")
  # find related document
  results = db.similarity_search(query, k = 2)
  # generate prompt
  for res in results:
    print(f"* {res.page_content} [{res.metadata}]")
  
    # give prompt to LLM
    # print answer


my_function("Dark Matter first discovery")

# sk-mopf2CVBnyslB1GzwzEaybYKsC41gN_8abShgZmZ-fT3BlbkFJd-TNV4SbEtyIVPOAhi8pVepIpKilwfnCC_QMwgxPAA
