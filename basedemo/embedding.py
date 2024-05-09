from IPython.utils import docs
from langchain_community.document_loaders import TextLoader
from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter, CharacterTextSplitter

raw_documents = TextLoader('./demo.txt',encoding="utf-8").load()

embeddings = OpenAIEmbeddings()

text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000,chunk_overlap=0)
#text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
documents = text_splitter.split_documents(raw_documents)
vector = FAISS.from_documents(documents, embeddings)

print(vector)