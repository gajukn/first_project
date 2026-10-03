from random import randint
import json
import os

# Файл для сохранения таблицы лидеров
LEADERBOARD_FILE = "leaderboard.json"

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
    # Ищем игрока в таблице
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
    
    # Сортируем по количеству попыток
    leaderboard.sort(key=lambda x: x['attempts'])
    return leaderboard

def main():
    print("=" * 45)
    print("🎯 ИГРА 'УГАДАЙ ЧИСЛО'")
    print("=" * 45)
    
    leaderboard = load_leaderboard()
    
    while True:
        print("\nМеню:")
        print("1. Играть")
        print("2. Показать таблицу лидеров")
        print("3. Выйти")
        
        choice = input("Выберите действие (1-3): ").strip()
        
        if choice == '1':
            player_name = input("Введите ваш ник: ").strip()
            if not player_name:
                print("⚠️  Ник не может быть пустым!")
                continue
            
            attempts = play_game(player_name)
            leaderboard = update_leaderboard(leaderboard, player_name, attempts)
            save_leaderboard(leaderboard)
            show_leaderboard(leaderboard)
        
        elif choice == '2':
            show_leaderboard(leaderboard)
        
        elif choice == '3':
            print("👋 До новых встреч!")
            break
        
        else:
            print("⚠️  Неверный выбор. Попробуйте снова.")

if __name__ == "__main__":
    main()