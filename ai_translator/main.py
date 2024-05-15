from ai_translator.components.md_printer import MDPrinter
from ai_translator.components.pdf_parser import PDFParser
from ai_translator.components.pdf_translator import PDFTranslator
from ai_translator.components.translator_config import TranslatorConfig
from ai_translator.lang_chain.llm_translator import LLMTranslator
from ai_translator.utils.argument_parser import ArgumentParser
from ai_translator.utils.logger import LOG

if __name__ == '__main__':
    #解析命令行参数
   argparse =  ArgumentParser()
   args = argparse.parse_arguments()

   #解析配置文件
   translator_config = TranslatorConfig()
   translator_config.initialize(args)

   # llm_translator = LLMTranslator()
   # result = llm_translator.run('this is an apple','english','chinese')
   # print(result[0])
   # translator = PDFTranslator(file_path = "D:/work/openai-quickstart/langchain/openai-translator/tests/The_Old_Man_of_the_Sea.pdf")
   # book = translator.translate()
   #
   # printer = MDPrinter(book)
   # printer.print()

