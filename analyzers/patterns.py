import re

PATTERNS = {
    "PASSPORT": r"\b\d{2}\s?\d{2}\s?\d{6}\b",
    "SNILS": r"\b\d{3}-\d{3}-\d{3}\s\d{2}\b",
    "PHONE": r"(?:\+7|8)[\s-]?\(?\d{3}\)?[\s-]?\d{3}[\s-]?\d{2}[\s-]?\d{2}",
    "BIRTHDAY": r"\b\d{2}\.\d{2}\.\d{4}\b",
    "EMAIL": r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
}
