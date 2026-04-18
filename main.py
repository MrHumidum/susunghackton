from pathlib import Path
from core.scanner import scan
from core.dispatcher import dispatch
from collections import defaultdict


def main():
    base = Path('./ПДнDataset/share')
    result = defaultdict(list)

    for file in scan(base):
        category = dispatch(file)
        result[category].append(file)

    for category, files in result.items():
        print(f"\n{category.upper()} ({len(files)}):")
        for f in files[:5]:
            print(f"  {f}")


if __name__ == "__main__":
    main()
