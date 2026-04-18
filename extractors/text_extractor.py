import fitz
from docx import Document
from striprtf.striprtf import rtf_to_text
import logging
from pathlib import Path


class TextExtractor:
    @staticmethod
    def get_text(file_path: Path) -> str:
        ext = file_path.suffix.lower()

        try:
            if ext == '.txt' or ext == '.md':
                return file_path.read_text(encoding='utf-8', errors='ignore')

            elif ext == '.docx':
                doc = Document(file_path)
                return "\n".join([p.text for p in doc.paragraphs])

            elif ext == '.pdf':
                text = ""
                with fitz.open(file_path) as doc:
                    for page in doc:
                        text += page.get_text()
                return text

            elif ext == '.rtf':
                content = file_path.read_text(
                    encoding='utf-8', errors='ignore')
                return rtf_to_text(content)

        except Exception as e:
            logging.error(f"Ошибка при извлечении из {file_path}: {e}")
            return ""

        return ""
