from ai_translator.book.book import Book


class MDPrinter:
    def __init__(self, book: Book):
        self.book = book
        book.pdf_file_path.replace(".pdf", "")
        self.output_file_path = f"{book.pdf_file_path}_translated.md"

    def print(self):
        with open(self.output_file_path, 'w', encoding='utf-8') as output_file:
            for page in self.book.pages:
                for content in page.contents:
                    output_file.write(content + '\n\n')
