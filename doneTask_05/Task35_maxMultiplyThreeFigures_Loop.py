def highest_product_of_3(list_of_ints):
    # Проверим, чтобы в массиве было 3 и больше чисел.
    if len(list_of_ints) < 3:
        raise Exception('Less than 3 items!')

    # Мы начнем с 3-его элемента массива (с индекса 2),
    # так как первые 2 элемента уже сразу пойдут
    # в highest_product_of_2 и lowest_product_of_2.
    highest = max(list_of_ints[0], list_of_ints[1])
    lowest = min(list_of_ints[0], list_of_ints[1])
    highest_product_of_2 = list_of_ints[0] * list_of_ints[1]
    lowest_product_of_2 = list_of_ints[0] * list_of_ints[1]

    # Также вычислим highest_product_of_three из первых 3-х элементов.
    highest_product_of_three = list_of_ints[0] * list_of_ints[1] * list_of_ints[2]

    # Начинаем проход по массиву с индекса 2.
    for current in list_of_ints[2:]:
        # проверяем возможность увеличить highest_product_of_three
        # или оставляем его как есть.
        highest_product_of_three = max(
            highest_product_of_three,
            current * highest_product_of_2,
            current * lowest_product_of_2)

        # То же самое проверим и на максимальном произведении из двух.
        highest_product_of_2 = max(
            highest_product_of_2,
            current * highest,
            current * lowest)

        # И на минимальном произведении из двух.
        lowest_product_of_2 = min(
            lowest_product_of_2,
            current * highest,
            current * lowest)

        # Появилось ли новое максимальное число?
        highest = max(highest, current)

        # Появилось ли новое минимальное число?
        lowest = min(lowest, current)

    return highest_product_of_three