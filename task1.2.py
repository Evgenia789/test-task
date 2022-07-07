def task(x1, y1, x2, y2, x3, y3, x4, y4):
    """
    Функция для определения пересечений двух прямоугольников.
    И вычисления площади пересечения, если такая имеется.
    """
    x11 = max(min(x1, x2), min(x3, x4))
    x12 = min(max(x1, x2), max(x3, x4))
    y11 = max(min(y1, y2), min(y3, y4))
    y12 = min(max(y1, y2), max(y3, y4))
    if (x12 - x11) > 0 and (y12 - y11) > 0:
        S = f'Площадь равна: {(x12 - x11) * (y12 - y11)}'
        return "\n".join(str(obj) for obj in (True, S))
    else:
        return False


if __name__ == '__main__':
    print(task(1, 1, 2, 2, 3, 3, 4, 4))
    print(task(1, 3, 5, 1, 5, 1, 9, 3))
    print(task(5, 3, 9, 1, 1, 1, 5, 3))
    print(task(1, 3, 5, 2, 1, 1, 5, 2))
    print(task(1, 2, 5, 1, 1, 2, 5, 3))
    print(task(1, 4, 4, 2, 5, 1, 8, 3))
    print(task(9, 4, 12, 2, 5, 1, 8, 3))
    print(task(7, 3, 11, 1, 2, 2, 6, 4))
    print(task(2, 3, 6, 1, 7, 2, 11, 4))
    print('-----------')
    print(task(2, 3, 6, 1, 4, 2, 8, 4))
    print(task(2, 4, 6, 2, 4, 1, 8, 3))
    print(task(3, 3, 7, 1, 1, 2, 5, 4))
    print(task(3, 4, 7, 2, 1, 1, 5, 3))
    print(task(1, 3, 5, 1, 4, 1, 8, 3))
    print(task(4, 3, 8, 1, 1, 1, 5, 3))
    print(task(1, 3, 5, 1, 1, 2, 5, 4))
    print(task(1, 4, 5, 2, 1, 1, 5, 3))
