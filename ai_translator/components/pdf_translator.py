from ai_translator.book.book import Book
from ai_translator.book.page import Page
from ai_translator.components.pdf_parser import PDFParser
from ai_translator.lang_chain.llm_translator import LLMTranslator
from ai_translator.utils.logger import Logger, LOG


class PDFTranslator:

    def translate(self, model_name: str = "gpt-3.5-turbo",source_language: str = "english"
                 , target_language: str = "chinese",file_path: str = None) -> Book:


        parser = PDFParser(file_path)
        translator = LLMTranslator(model_name)

        book = parser.parse()

        book_translated = Book(file_path)

        LOG.info('翻译文件开始...')
        for page in book.pages:
            for content in page.contents:
                text = translator.run(content.text, source_language, target_language)

                LOG.info(text)

                page = Page()
                page.add_content(text)
                book_translated.add_page(page)

        return book_translated