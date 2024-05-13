from ai_translator.components.translator_config import TranslatorConfig
from ai_translator.lang_chain.llm_translator import LLMTranslator
from ai_translator.utils.argument_parser import ArgumentParser

if __name__ == '__main__':
    #解析命令行参数
   argparse =  ArgumentParser()
   args = argparse.parse_arguments()

   #解析配置文件
   translator_config = TranslatorConfig()
   translator_config.initialize(args)

   llm_translator = LLMTranslator()
   result = llm_translator.run('this is an apple','english','chinese')
   print(result[0])