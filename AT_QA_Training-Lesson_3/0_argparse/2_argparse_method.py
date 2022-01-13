import argparse

parser = argparse.ArgumentParser()

"""
    Все параметры для add_argument
    
    name or flags - либо имя, либо список строк параметров, например. foo или -f, --foo..
    action - основной тип действия, которое необходимо предпринять, когда этот аргумент встречается в командной строке..
    nargs - количество аргументов командной строки, которые следует использовать.
    const - постоянное значение, необходимое для выбора некоторых действий и nargs.
    default - Значение, создаваемое, если аргумент отсутствует в командной строке.
    type - Тип, в который должен быть преобразован аргумент командной строки.
    choices - контейнер допустимых значений для аргумента.
    required - можно ли опустить параметр командной строки (только необязательные параметры).
    help - Краткое описание того, что делает аргумент.
    metavar - имя аргумента в сообщениях об использовании.
    dest - имя атрибута, который будет добавлен к объекту, возвращаемому функцией parse_args().

"""

parser.add_argument('--method', '-m',
                    action='store',
                    help='Method to make request',
                    default='GET')

parser.add_argument('--url', '-u',
                    action='store',
                    help='Url to make request to',
                    required=True)

# Если параметр передан то Ture, иначе False
parser.add_argument('--true', '-t',
                    action='store_true',
                    help='True or false param',
                    required=False)

# Добавляение значений в список по параметру
# python3 2_argparse_method.py --url=ya.ru -s
parser.add_argument('--save', '-s',
                    action='append_const',
                    const='const_to_save',
                    dest='const_collection',
                    default=[],
                    help='Store params in list',
                    required=False)

# Добавляение значений в список по параметру
# python3 2_argparse_method.py --url=ya.ru -s -s2
parser.add_argument('--save2', '-s2',
                    action='append_const',
                    const='const_to_save2',
                    dest='const_collection',
                    default=[],
                    help='Store params in list',
                    required=False)

# Парсим всё что положили
args = parser.parse_args()

# Это словарь из которого аргументы можно доставать
print(args)
