import csv
import pandas as pd
from typing import Any


def transactions_csv_file(filename: str) -> Any:
    ''' Функция, считывающая финансовые операции из CSV-файлов '''
    transactions = []
    try:
        with open(f'{filename}', encoding="utf-8") as file_csv:
            reader = csv.DictReader(file_csv, delimiter=';')
            for row in reader:
                transactions.append(row['description'])
            return transactions
    except Exception as error:
        return f'Ошибка: {error}'
    return ''


print(transactions_csv_file('..\\files\\transactions.csv'))


def transactions_xlsx_file(filename: str) -> Any:
    ''' Функция, считывающая финансовые операции из XLSX-файлов '''
    try:
        excel_file = pd.read_excel(f'{filename}')
        return excel_file
    except Exception as error:
        return f'Ошибка: {error}'
    return ''


print(transactions_xlsx_file('..\\files\\transactions_excel.xlsx'))
