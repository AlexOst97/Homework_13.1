# Проект 'python_project_dz2'

## Цель проекта:

Программа для фильтрации и сортировки банковских счетов по дате и оплате.

## Инструкция по установке:

- python = "3.13"
- flake8 = "7.1.1"
- mypy = "1.13.0"
- isort = "5.13.2"
- black = "24.10.0"
- requests = "^2.32.3"
- python-dotenv = "^1.0.1"
- pandas = "^2.2.3"
- openpyxl = "^3.1.5"

## Использование:

- Функция скрывающая номер карты;
- Функция скрывающая номер счета;
- Функция сортировки выполнения операции;
- Функция сортировки операций по дате;
- Функция,которая принимает на вход список словарей, представляющих транзакции;
- Генератор, который принимает список словарей с транзакциями и возвращает описание каждой операции по очереди;
- Генератор, который выдает номера банковских карт в формате *XXXX XXXX XXXX XXXX*;
- Декоратор, который будет автоматически логировать начало и конец выполнения функции, а также ее результаты или возникшие ошибки;
- функция, которая принимает на вход путь до JSON-файла и возвращает список словарей с данными о финансовых транзакциях;
- Функция, которая принимает на вход транзакцию и возвращает сумму транзакции в рублях;
- Функция, считывающая финансовые операции из *CSV*-файлов;
- Функция, считывающая финансовые операции из *XLSX*-файлов.


## Тестирование проекта:

Тестирование функций проекта осуществляется с помощью фреймворка **pytest** и метрики **code coverage**.
Для этого установлены расширения:
- pytest = "^8.3.3"
- pytest-cov = "^6.0.0"

## Инструкция по установке:

1. Клонировать с GitHab (git clone https://github.com/AlexOst97/python_project_dz2.git)
2. Установить зависимости (pip install -r requirements.txt)

## Команда проекта:

- Останин Александр (*aostanin97@gmail.com*) - **backend developer** 

## Источники

Программа создана при поддержке онлайн-школы
![Программа создана при поддержке онлайн-школы](https://digital-academy.ru/foto/school/skypro-2.png)