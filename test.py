## Retreival Augmented Generation 

import os
from dotenv import load_dotenv
load_dotenv()

import os.path
from llama_index import(
    VectorStoreIndex,
    SimpleDirectoryReader,
    load_index_from_storage,
)

os.environ['OPENAI_API_KEY']=os.getenv("OPENAI_API_KEY")

from llama_index import VectorStoreIndex,SimpleDirectoryReader
documents=SimpleDirectoryReader("data").load_data()

documents

index=VectorStoreIndex.from_documents(documents,show_progress=True)

index

query_engine=index.as_query_engine()

response=query_engine.query("What is transformers")

from llama_index.retrievers import VectorIndexRetriever
from llama_index.query_engine import RetrieverQueryEngine 
from llama_index.indices.postprocessor import SimilarityPostprocessor

retriever = VectorIndexRetriever(index=index,similarity_top_k=4)
postprocessor=SimilarityPostprocessor(similarit,cutoff=0.80)
query_engine=index.as_query_engine()

query_engine = RetrieverQueryEngine(retriever=retriever,node_postprocessors=postprocessor)

from llama_index.response.pprint_utils import pprint_response
pprint_response(response)
print(response)

# check if storage already exists 

PERSIST_DIR = "./storage"
if not os.path.exists(PERSIST_DIR):
    # load he documents and create the index 
    documents=SimpleDirectoryReader("data").load_Data()
    index=VectorStoreIndex.from_documents(documents)
    # store it for later
    index.storage_context.persist(persist_dir=PERSIST_DIR)

else:
    #load the existing index
    storage_context = StorageContext.from_defaults(persist_dir=PERSIST_DIR)
    index=load_index_from_storage(storage_context)

    # either way we can now query the index 
    query_engine = index.as_query_engine()
    response=query_engine.query("What is transformers?")
    print(response)

