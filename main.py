import csv
import re
from pathlib import Path
from collections import defaultdict

from core.scanner import scan
from core.dispatcher import dispatch
from extractors.text_extractor import TextExtractor
from analyzers.patterns import PATTERNS
from analyzers.validators import validate_snils


def analyze_content(text):
    findings = defaultdict(int)
    if not text:
        return findings

    for label, pattern in PATTERNS.items():
        matches = re.findall(pattern, text)
        for match in matches:
            if label == "SNILS" and not validate_snils(match):
                continue
            findings[label] += 1
    return findings


def determine_uz(findings):
    if not findings:
        return "УЗ-4"

    if findings.get("PASSPORT") or findings.get("SNILS"):
        return "УЗ-3"

    return "УЗ-4"


def main():
    base_dir = Path('./ПДнDataset/share')
    report_file = Path('result.csv')

    if not base_dir.exists():
        print(f"Ошибка: Директория {base_dir} не найдена!")
        return

    headers = ['путь', 'категории ПДн',
               'количество_находок', 'УЗ', 'формат файла']

    print(f"--- Запуск полного сканирования: {base_dir} ---")

    with open(report_file, mode='w', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=headers)
        writer.writeheader()

        for file_path in scan(base_dir):
            file_ext = file_path.suffix.lower()

            content = TextExtractor.get_text(file_path)

            findings = analyze_content(content)

            uz_level = determine_uz(findings)

            categories_str = ", ".join(findings.keys()) if findings else "Нет"
            total_count = sum(findings.values())

            writer.writerow({
                'путь': str(file_path),
                'категории ПДн': categories_str,
                'количество_находок': total_count,
                'УЗ': uz_level,
                'формат файла': file_ext
            })

            if total_count > 0:
                print(f"[!] ПДн найдены: {file_path.name} ({total_count} шт.)")

    print(f"\nАнализ завершен. Отчет сохранен в: {report_file}")


if __name__ == "__main__":
    main()
