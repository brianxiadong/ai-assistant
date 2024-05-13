from ai_translator.components.translator_config import TranslatorConfig
from ai_translator.utils.argument_parser import ArgumentParser

if __name__ == '__main__':
    #解析命令行参数
   argparse =  ArgumentParser()
   args = argparse.parse_arguments()

   #解析配置文件
   translator_config = TranslatorConfig()
   translator_config.initialize(args)


