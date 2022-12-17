import argparse

text = '''
===== Калькулятор =====
'''.strip()


def calc(x, y):
    print(text)
    res = x + y
    print(f'{x} + {y} = {res}', end='\n\n')

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Калькулятор') # Создаем парсер для аргументов, переданных через командную строку
    parser.add_argument('x', type=int, help='Первое число')   # Задаем один обязательный аргумент - имя
    parser.add_argument('y', type=int, help='Второе число')
    args = parser.parse_args()
    x = args.x
    y = args.y
    calc(x, y)