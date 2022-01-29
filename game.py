import numpy as np

def random_predict(number: int = 1) -> int:
    """Используя алгоритм бинарного поиска угадывает число
       Принимает загаданное число из отрезка [1;100] и возвращает кол-во попыток.
    

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Количество попыток
    """
    count = 1
    low = 1
    high = 100
    predict_number = 50

    while True:
        if predict_number > number:
            high = predict_number - 1
        elif predict_number < number:
            low = predict_number + 1
            
        if number == predict_number:
            return count

        predict_number = (low+high) // 2
        count += 1

def score_game(random_predict) -> int:
    """За какое количество попыток в среднем за 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    np.random.seed(2022)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000)) # список для чисел  

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls))
    return score
    

print(score_game(random_predict))