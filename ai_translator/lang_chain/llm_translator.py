from langchain import hub
from langchain_openai import ChatOpenAI


class LLMTranslator:
    def __init__(self, model_name: str = "gpt-3.5-turbo"):
        # Get the prompt to use - you can modify this!
        prompt = hub.pull("brianxiadong/ai-translator-prompt")
        # 为了翻译结果的稳定性，将 temperature 设置为 0
        chat = ChatOpenAI(model_name=model_name, temperature=0)
        self.chain = prompt | chat

    def run(self,text: str, source_language: str, target_language: str) -> (str,bool):
        result = self.chain.invoke({
            "text": text,
            "source_language": source_language,
            "target_language": target_language,
        })

        return result.content,True