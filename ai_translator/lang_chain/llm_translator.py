from langchain import hub
from langchain_core.prompts import SystemMessagePromptTemplate, HumanMessagePromptTemplate, ChatPromptTemplate
from langchain_openai import ChatOpenAI


class LLMTranslator:
    def __init__(self, model_name: str = "gpt-3.5-turbo"):

        # 翻译任务指令始终由 System 角色承担
        template = (
            """You are a translation expert, proficient in various languages. \n
            Translates {source_language} to {target_language}."""
        )
        system_message_prompt = SystemMessagePromptTemplate.from_template(template)

        # 待翻译文本由 Human 角色输入
        human_template = "{text}"
        human_message_prompt = HumanMessagePromptTemplate.from_template(human_template)

        # 使用 System 和 Human 角色的提示模板构造 ChatPromptTemplate
        prompt = ChatPromptTemplate.from_messages(
            [system_message_prompt, human_message_prompt]
        )

        # hub上的prompt不稳定
        #prompt = hub.pull("brianxiadong/ai-translator-prompt")
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