import random

truth_count = 0
action_count = 0

while True:
    print("Если выбираете сказать правду, нажмите 1, если выбираете действие, нажмите 2. Нажмите 3, чтобы выйти.")
    choice = int(input("Ваш выбор: "))

    if choice == 1:
        truth_count += 1
        truths = ["Какой ваш любимый фильм?", "Какое ваше хобби?", "Какое ваше самое забавное детское воспоминание?"]
        random_truth = random.choice(truths)
        print(f"Правда: {random_truth}")

    elif choice == 2:
        action_count += 1
        actions = ["Покажите свой лучший танец.", "Опишите самое страшное, что вы когда-либо делали.", "Сфотографируйтесь соседом."]
        random_action = random.choice(actions)
        print(f"Действие: {random_action}")

    elif choice == 3:
        print(f"Статистика: было выбрано {truth_count} вопросов и {action_count} действий")
        break

    else:
        print("Неверный ввод. Попробуйте снова.")
