import random

def game():
    stones = random.randint(-20, 20) # Начальное количество камней в куче
    attempt = 0
    print("Добро пожаловать в игру 'Каменная куча'!")
    print("В куче сейчас", stones, "камней.")


    while stones != 0: # Игра продолжается, пока в куче есть камни
        action = input("Выберите действие: [1] Вычесть число, [2] Прибавить число, [3] Узнать количество камней в куче: ")

        if action == '1':
            num = random.randint(1, 10) # Случайное число для вычитания
            print("Вы вычитаете", num, "камней из кучи.")
            stones -= num
            attempt += 1
        elif action == '2':
            num = random.randint(1, 10) # Случайное число для прибавления
            print("Вы добавляете", num, "камней в кучу.")
            stones += num
            attempt += 1
        elif action == '3':
            print(f"Количество камней в куче в данный момент: {stones}")

    print("В куче теперь", stones, "камней.")

    print(f"Поздравляем, вы победили за {attempt} попыток!")

game()