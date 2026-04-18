import pandas as pd
from pathlib import Path
import logging

def extract_table(file_path: Path) -> str:
    try:
        suffix = file_path.suffix.lower()

        if suffix == ".csv":
            df = pd.read_csv(file_path, dtype=str)

        elif suffix == ".json":
            df = pd.read_json(file_path, dtype=str)

        elif suffix in {".xls", ".xlsx"}:
            df = pd.read_excel(file_path, dtype=str)

        elif suffix == ".parquet":
            df = pd.read_parquet(file_path)

        else:
            return "NO_EXTENSION"

        df = df.fillna('')

        text = "\n".join(
            df.apply(lambda row: " ".join(map(str, row.values)), axis=1)
        )

        return text

    except Exception as e:
        logging.error(f"Ошибка чтения таблицы {file_path}: {e}")
        return ""