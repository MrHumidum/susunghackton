from pathlib import Path
import logging

EXCLUDED_DIRS = {".git", "__pycache__", "node_modules"}


def scan(base_path: Path):
    for path in base_path.rglob('*'):
        try:
            if any(part in EXCLUDED_DIRS for part in path.parts):
                continue

            if path.is_file():
                yield path

        except PermissionError as e:
            logging.error(f"Нет доступа: {path} ({e})")
