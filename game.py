import numpy as np

number = np.random.randint(0, 101) 

def random_predict(number):
    """Игра угадай число.
Компьютер сам загадывает и угадывает число
"""
    count = 0
    min, max = 0, 100
    print('Загаданное число: ', number)
    
    predict_number = 50 # предполагаемое число

    while number != predict_number:
        count+=1
        if number == 100:
            return(count)
        # сужаем рамки поиска
        if number > predict_number:
            min = predict_number # Устанавливаем новый минимальный предел
            print('min: ', predict_number)
            
        else:
            max = predict_number # Устанавливаем новый максимальный предел
            print('max: ', predict_number)
            
            
        predict_number = int((max + min ) / 2) # разбиваем по полам новые рамки поиска
            
    return(count)

print(f'Количество попыток: {random_predict(number)}')

def score_game(random_predict) -> int:
    """За какое количство попыток в среднем за 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    #np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000))  # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за:{score} попыток")
    return score
