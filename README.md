![Python](https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue)
![tkinter](https://img.shields.io/badge/tkinter-3776AB?style=for-the-badge&logo=python&logoColor=white)
![pyperclip](https://img.shields.io/badge/pyperclip-3776AB?style=for-the-badge&logo=python&logoColor=white)

# Парсер буфера обмена

Десктопное приложение на Python для парсинга путей из буфера обмена с группировкой и сортировкой.

## Установка

1. Установите зависимости:
```bash
pip install -r requirements.txt
```

## Запуск

```bash
python main.py
```

## Использование

1. Скопируйте пути к папкам в буфер обмена
2. Нажмите кнопку "Вставить из буфера"
3. Приложение:
   - Проверит наличие текста в буфере обмена
   - Покажет количество строк в буфере
   - Распарсит пути, извлекая предпоследнюю и последнюю папку из каждого пути
   - Удалит все кавычки из путей
   - Сгруппирует результаты по предпоследней папке
   - Отсортирует группы по предпоследней папке, а внутри группы - по последней папке
   - Выведет результат в текстовое поле в следующем формате:
     - Название группы (предпоследняя папка) на отдельной строке
     - Список последних папок с табуляцией на следующих строках
     - Пустая строка между группами
   - Покажет количество выведенных последних папок (без учета групп и пустых строк)

## Пример вывода

```
группа1
    папка1
    папка2
    папка3

группа2
    папка4
    папка5
```

## Технологии

- Python 3
- tkinter - для графического интерфейса
- pyperclip - для работы с буфером обмена



2025 by Vladimir Papin ![image](https://img.shields.io/badge/Gmail-EA4335?style=flat&logo=gmail&logoColor=white) ![image](https://img.shields.io/badge/Telegram-26A5E4?style=flat&logo=telegram&logoColor=white)

