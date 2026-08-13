# Index is a specific data structure used to organize a collection of nodes for optimized storage and retrieval.
# It is just packing related items together.

# Some types of indexes in LlamaIndex: SummaryIndex, DocumentSummaryIndex, VectorStoreIndex, TreeIndex, KeywordTableIndex, KnowledgeGraphIndex, ObjectIndex, ComposableGraph

# Let's consider a simple example to illustrate the creation of SummaryIndex
from llama_index.core import SummaryIndex, Document
from llama_index.core.node_parser import SentenceSplitter
from llama_index.llms.ollama import Ollama

llm = Ollama(
    model="gemma4:e2b",
    request_timeout=120.0,
)

doc = Document(text=(
    "Lionel Messi is a football player from Argentina. "
    "He has won the Ballon d'Or trophy 8 times. "
    "Lionel Messi's hometown is Rosario. "
    "He was born on June 24, 1987."
))
splitter = SentenceSplitter(chunk_size=20, chunk_overlap=0)
nodes = splitter.get_nodes_from_documents([doc])
index = SummaryIndex(nodes)

query_engine = index.as_query_engine(llm=llm)
response = query_engine.query("What is Messi's hometown?")
print(response)
