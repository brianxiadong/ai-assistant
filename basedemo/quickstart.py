from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

llm = ChatOpenAI()
#llm = ChatOpenAI(api_key="...")

output_parser = StrOutputParser()

#llm.invoke("how can langsmith help with testing?")

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a world class technical documentation writer."),
    ("user", "{input}")
])

chain = prompt | llm | output_parser

result = chain.invoke({"input": "how can langsmith help with testing?"})

print(result)



