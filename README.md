# Парсер статей с Pedsovet.org

## Описание проекта
Программа парсит главную страницу образовательного портала Pedsovet.org и извлекает информацию о статьях:
- **Наименования статей**
- **Ссылки на полные версии статей**

## Источник данных
HTML-страница загружается напрямую с сайта: **https://pedsovet.org/**

Программа автоматически:
- **Загружает главную страницу**
- **Находит все ссылки на статьи**
- **Фильтрует только уникальные записи**
- **Обрабатывает относительные ссылки**
- **Сохраняет результаты в структурированном формате**

### Запуск

# Клонируйте репозиторий
git clone https://github.com/Valeriyakos/pedsovet_parser

# Перейдите в папку проекта
cd pedsovet_parser

# Установите зависимости и запустите
py -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
py parse_pedagogy.py

### Пример использования
`py parse_pedagogy.py`
Найдено: 27

1. Не списывание, а новый навык: нейросети в школьных работах
   https://pedsovet.org/article/ne-spisyvanie-a-novyj-navyk-nejroseti-v-skolnyh-rabotah

2. Кинолог: плюсы и минусы профессии
   https://pedsovet.org/article/kinolog-plusy-i-minusy-professii

3. Почему важны диалоги в развитии речи ребенка
   https://pedsovet.org/article/pocemu-vazny-dialogi-v-razvitii-reci-rebenka

4. Как помочь новенькому освоиться в детском саду
   https://pedsovet.org/article/kak-pomoc-novenkomu-osvoitsa-v-detskom-sadu

5. Кинезиотерапия: зачем она нужна и как организовать занятия
   https://pedsovet.org/article/kinezioterapia-zacem-ona-nuzna-i-kak-organizovat-zanatia
...



### Результат работы
Программа сохраняет данные в файл `articles.json` в формате:

[
  {
    "name": "Название статьи",
    "link": "https://pedsovet.org/ссылка-на-статью"
  }
]

### Используемые технологии
- Python 3.x
- BeautifulSoup4 - парсинг HTML
- Requests - HTTP-запросы


### Структура проекта

`parse_pedagogy.py`    # Основной скрипт парсера
`requirements.txt`     # Список зависимостей
`README.md`           # Документация
`.gitignore`          # Исключаемые файлы
`articles.json`       # Результат работы (создается автоматически)