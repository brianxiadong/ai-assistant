import pdfplumber

from ai_translator.book.book import Book
from ai_translator.book.content import Content
from ai_translator.book.page import Page
from ai_translator.utils.logger import LOG


class PDFParser:
    def __init__(self, file_path: str):
        self.book = Book(file_path)

    def parse(self) -> Book:
        LOG.info('读取文件开始...')
        with pdfplumber.open(self.book.pdf_file_path) as pdf:
            count = 0
            for page in pdf.pages:
                if count == 2:
                    break
                raw_text = page.extract_text()
                # Remove empty lines and leading/trailing whitespaces
                raw_text_lines = raw_text.splitlines()
                cleaned_raw_text_lines = [line.strip() for line in raw_text_lines if line.strip()]
                cleaned_raw_text = "\n".join(cleaned_raw_text_lines)

                LOG.info(cleaned_raw_text)

                if len(cleaned_raw_text) < 3:
                    continue

                content = Content()
                content.add_text(cleaned_raw_text)
                new_page = Page()
                new_page.add_content(content)
                self.book.add_page(new_page)
                count += 1

        return self.book
