import requests
import json
import urllib.request
import os

with urllib.request.urlopen("https://raw.githubusercontent.com/Aporial/Svitlo_Sumy/main/database/database_test.json") as url:
    main_database = json.load(url)
file = 'database/database_test.json'
INDEX_FILE = 'last_index.json'

# URL API для моніторингу
API_URL = 'https://www.soe.com.ua/includes/vidklyuchennya_srv_CURL.php?cmd=get_user_disconnections_image_api&cherga=2'


def fetch_data(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print(f"Помилка запиту до {url}: {e}")
        return None


def load_last_index():
    if os.path.exists(INDEX_FILE):
        with open(INDEX_FILE, 'r') as file:
            data = json.load(file)
            return data.get('last_index', 0)
    return 0


def save_last_index(index):
    with open(INDEX_FILE, 'w') as file:
        json.dump({'last_index': index}, file)


def cleanup():
    # Видалення файлу з індексом
    if os.path.exists(INDEX_FILE):
        os.remove(INDEX_FILE)
        print(f"Файл {INDEX_FILE} видалено.")


def update_database(begin_hour, end_hour):
    today = 4
    one = [1, 7, 13, 19, 25]
    two = [2, 8, 14, 20, 26]
    three = [3, 9, 15, 21, 27]
    four = [4, 10, 16, 22, 28]
    five = [5, 11, 17, 23, 29]
    six = [6, 12, 18, 24, 30]
    seven = [31]
    if today in one:
        day_prefix = 'one'
    if today in two:
        day_prefix = 'two'
    if today in three:
        day_prefix = 'three'
    if today in four:
        day_prefix = 'four'
    if today in five:
        day_prefix = 'five'
    if today in six:
        day_prefix = 'six'
    if today in seven:
        day_prefix = 'seven'
    last_index = load_last_index()
    new_index = last_index + 1
    day_num_key = f'{day_prefix}_{new_index}'
    print(day_num_key)
    main_database["1_cherg"][day_num_key] = f"{begin_hour}-{end_hour}"
    save_last_index(new_index)
    with open(file, 'w', encoding='utf-8') as new_file:
        json.dump(main_database, new_file, ensure_ascii=False, indent=4)


data = fetch_data(API_URL)
if data:
    # Отримання значення поля "items_hour_disc"
    items_hour_disc = data.get('data').get('items_hour_disc')

    # Форматування та збереження даних
    formatted_times = []

    for item in items_hour_disc:
        begin_hour = item.get('begin_hour')
        end_hour = item.get('end_hour')
        update_database(begin_hour, end_hour)

    # Збереження результатів у файл
else:
    print("Не вдалося отримати дані з API")

cleanup()
