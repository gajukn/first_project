from random import randint
import json
import os

LEADERBOARD_FILE = "leaderboard.json"
LAST_PLAYER_FILE = "last_player.json"


def load_leaderboard():
    """Загружает таблицу лидеров из файла"""
    if os.path.exists(LEADERBOARD_FILE):
        try:
            with open(LEADERBOARD_FILE, 'r', encoding='utf-8') as f:
                return json.load(f)
        except (json.JSONDecodeError, IOError):
            return []
    return []


def save_leaderboard(leaderboard):
    """Сохраняет таблицу лидеров в файл"""
    with open(LEADERBOARD_FILE, 'w', encoding='utf-8') as f:
        json.dump(leaderboard, f, ensure_ascii=False, indent=2)


def load_last_player():
    """Загружает последний использованный ник"""
    if os.path.exists(LAST_PLAYER_FILE):
        try:
            with open(LAST_PLAYER_FILE, 'r', encoding='utf-8') as f:
                data = json.load(f)
                return data.get('name', '')
        except (json.JSONDecodeError, IOError):
            return ''
    return ''


def save_last_player(name):
    """Сохраняет последний использованный ник"""
    with open(LAST_PLAYER_FILE, 'w', encoding='utf-8') as f:
        json.dump({'name': name}, f, ensure_ascii=False, indent=2)


def show_leaderboard(leaderboard):
    """Показывает таблицу лидеров"""
    if not leaderboard:
        print("\n📋 Таблица лидеров пока пуста.")
        return

    print("\n" + "=" * 45)
    print("🏆 ТАБЛИЦА ЛИДЕРОВ")
    print("=" * 45)
    print(f"{'Место':<7}{'Игрок':<20}{'Попытки':<10}")
    print("-" * 45)
    for i, entry in enumerate(leaderboard[:10], 1):
        print(f"{i:<7}{entry['name']:<20}{entry['attempts']:<10}")
    print("=" * 45 + "\n")


def play_game(player_name):
    """Основная логика игры"""
    number = randint(1, 100)
    attempts = 0

    print(f'\n🎮 {player_name}, угадайте число от 1 до 100')

    while True:
        try:
            guess = int(input('Введите число: '))
        except ValueError:
            print('⚠️  Пожалуйста, введите целое число!')
            continue

        attempts += 1

        if guess < number:
            print('📉 Ваше число меньше того, что загадано.')
        elif guess > number:
            print('📈 Ваше число больше того, что загадано.')
        elif guess == number:
            break

    print(f'\n🎉 Отличная интуиция, {player_name}! Вы угадали число за {attempts} попыток!')
    return attempts


def update_leaderboard(leaderboard, player_name, attempts):
    """Обновляет таблицу лидеров"""
    found = False
    for entry in leaderboard:
        if entry['name'] == player_name:
            found = True
            if attempts < entry['attempts']:
                entry['attempts'] = attempts
                print(f'✨ Новый личный рекорд: {attempts} попыток!')
            break

    if not found:
        leaderboard.append({'name': player_name, 'attempts': attempts})

    leaderboard.sort(key=lambda x: x['attempts'])
    return leaderboard


def ask_player_name(last_player):
    """Запрашивает ник, предлагая последний использованный"""
    if last_player:
        answer = input(f"Введите ваш ник (Enter — '{last_player}'): ").strip()
        if not answer:
            return last_player
        return answer
    else:
        while True:
            name = input("Введите ваш ник: ").strip()
            if name:
                return name
            print("⚠️  Ник не может быть пустым!")


def main():
    print("=" * 45)
    print("🎯 ИГРА 'УГАДАЙ ЧИСЛО'")
    print("=" * 45)

    leaderboard = load_leaderboard()
    last_player = load_last_player()

    if last_player:
        print(f"👋 С возвращением, {last_player}!")

    while True:
        print("\nМеню:")
        print("1. Играть")
        print("2. Показать таблицу лидеров")
        print("3. Выйти")

        choice = input("Выберите действие (1-3): ").strip()

        if choice == '1':
            player_name = ask_player_name(last_player)
            last_player = player_name

            attempts = play_game(player_name)
            leaderboard = update_leaderboard(leaderboard, player_name, attempts)
            save_leaderboard(leaderboard)
            show_leaderboard(leaderboard)

        elif choice == '2':
            show_leaderboard(leaderboard)

        elif choice == '3':
            # Сохраняем последний ник перед выходом
            if last_player:
                save_last_player(last_player)
                print(f"💾 Ваш ник сохранён: {last_player}")
            print(f"👋 До новых встреч, {last_player}!" if last_player else "👋 До новых встреч!")
            break

        else:
            print("⚠️  Неверный выбор. Попробуйте снова.")


if __name__ == "__main__":
    main()