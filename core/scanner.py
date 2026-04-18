from pathlib import Path
import logging


def scan(base_path: Path):
    for path in base_path.rglob('*'):
        try:
            if path.is_file():
                yield path

        except PermissionError as e:
            logging.error(f"Нет доступа: {path} ({e})")
