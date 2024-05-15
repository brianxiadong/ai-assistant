import sys
import os
import gradio as gr

from ai_translator.components.pdf_translator import PDFTranslator
from ai_translator.components.translator_config import TranslatorConfig
from ai_translator.utils import ArgumentParser

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

def translation(input_file, source_language, target_language):

    output_file_path = Translator.translate(
        input_file.name, source_language=source_language, target_language=target_language)

    return output_file_path

def launch_gradio():

    iface = gr.Interface(
        fn=translation,
        title="PDF-Translator v1.0",
        inputs=[
            gr.File(label="上传PDF文件"),
            gr.Textbox(label="源语言（默认：英文）", placeholder="English", value="English"),
            gr.Textbox(label="目标语言（默认：中文）", placeholder="Chinese", value="Chinese")
        ],
        outputs=[
            gr.File(label="下载翻译文件")
        ],
        allow_flagging="never"
    )

   # iface.launch(share=True, server_name="0.0.0.0")
    iface.launch()
def initialize_translator():
    # 解析命令行参数
    argparse = ArgumentParser()
    args = argparse.parse_arguments()

    # 解析配置文件
    translator_config = TranslatorConfig()
    translator_config.initialize(args)

    global Translator
    Translator = PDFTranslator()


if __name__ == "__main__":
    # 初始化 translator
    initialize_translator()
    # 启动 Gradio 服务
    launch_gradio()
