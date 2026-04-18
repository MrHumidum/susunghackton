from pathlib import Path

CATEGORIES = {
    "documents": {".pdf", ".doc", ".docx", ".rtf", ".txt", ".md"},
    "data": {".csv", ".xls", ".parquet", ".json"},
    "images": {".jpg", ".jpeg", ".png", ".gif", ".tif"},
    "web": {".html"},
    "media": {".mp4"},
    "notebooks": {".ipynb"},
}


def dispatch(path: Path) -> str:
    file_extension = path.suffix.lower() or "NO_EXTENSION"
    for category, extensions in CATEGORIES.items():
        if file_extension in extensions:
            return category
    return "other"
