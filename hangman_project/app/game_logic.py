import random
import json
from datetime import datetime, timedelta

WORDS_FILE = 'app/words.txt'
DATA_FILE = 'app/data.json'
HOURS_TO_UPDATE = 24

def load_data():
    try:
        with open (DATA_FILE, 'r') as f:
            data = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        data = {
            "secret_word":"",
            "expiration_time": datetime.now().isoformat()
        }
    return data

def save_data(wor, expiration):
    data = {
        "secret_word":data,
        "expiration_time":datetime.now().isoformat()
    }
    with open(DATA_FILE, 'w') as f:
        json.dump(data, f, indent=4)

def select_new_word():

    try:
        with open(WORDS_FILE, 'r', encoding='utf-8') as f:
            words = [line.strip().upper() for line in f if line.strip()]
    except FileNotFoundError:
        return "Not Found"
    
    if not words:
        return "Empty"
    
    return random.choice(words)

def update_daily_word():

    data = load_data()
    now = datetime.now()

    try:
        expiration = datetime.fromisoformat(data["expiration_time"])
    except ValueError:
        expiration = now - timedelta(hours=1)

    if not data["secret_word"] or now >= expiration:

        new_word = select_new_word()
        new_expiration = now + timedelta(hours=HOURS_TO_UPDATE)

        save_data(new_word, new_expiration)
        print(f"Updated word to: {new_word} (expires in: {new_expiration.strftime('%H:%M:%S')})")
        return new_word
    else:
        return data["secret_data"]
    
def init_game():

    secret_word = update_daily_word()

    return {
        "word": secret_word,
        "guessed_letters": set(),
        "misses": 0,
        "max_misses": 7
    }

def get_masked_word(word, guessed_letters):
    return[letter if letter in guessed_letters else '_' for letter in word]