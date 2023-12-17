# Задание - фильтрация текста

def validate(values_list): # Проверка ввода
    global choise
    choise = input("Введите значение: ").lower()
    while choise not in values_list:
        choise = input(f"Выберите одно из предложенных значений: {values_list}\nВвод: ").lower()
    return choise

def menu(): # Меню фильтров
    print("\nМеню фильтров:")
    for i in range(len(filters)):
        print(f"{i}: {filters[i]["name"]}")
    print ("Выберите фильтр (или 0 для выхода)")
    validate (str(["0 1 2 3 4 5"]))


def camel_filter(text):
    result = ""
    is_next_upper = False
    for i in range(len(text)):
        if i == 0:
            result += text[i].upper()
        elif text[i] == " ":
            is_next_upper = True
        elif is_next_upper:
            result += text[i].upper()
            is_next_upper = False
        else:
            result += text[i]
    return result



def python_filter(text):
    return text.replace(" ", "_")

def shout_filter(text):
    return text.upper()

def whisper_filter(text):
    return text.lower()

def snake_filter(text):
    result = ""
    s = "-с-с"
    sh = "-ш-ш"
    for i in range(len(text)):
        if text[i].lower() == "с":
            result += text[i] + s
        elif text[i].lower() == "ш":
            result += text[i] + sh
        else:
            result += text[i]
    return result

def exit():
    print("До свидания!")

filters = {     #Список фильтров
    0: {
        "name": "Выход",
        "function": exit,
    },
    1: {
        "name": "ВерблюжийФильтр:",
        "description": "Текст без пробела и первая буква каждого слова заглавная.",
        "function": camel_filter,
    },

    2: {
        "name": "Питоний_фильтр:",
        "description": "Заменяет пробелы в тексте на '_'(нижнее подчеркивание).",
        "function": python_filter,
    },

    3: {
        "name": "КРИЧАЩИЙ ФИЛЬТР:",
        "description": "Преобразует все буквы текста в заглавные.",
        "function": shout_filter,
    },

    4: {
        "name": "шепчущий фильтр:",
        "description": "Преобразует все буквы текста в строчные.",
        "function": whisper_filter,
    },

    5: {
        "name": "Змеиный фильтр:",
        "description": "Если в тексте есть буквы 'с' и 'ш' он их удваивает (Например: Сос - С-с-сос-с-с)." ,
        "function": snake_filter,
    }
}

menu()
while choise != "0":
    for i in choise:
        print(f"\n{filters[int(i)]["name"]}")
        print(f"{filters[int(i)]["description"]}")
    print("\nПрименить фильтр к тексту (Да, Нет)?")
    validate(["да", "нет"])
    if choise == "да":
        vvod = input("Ведите текст для фильтрации: ")
        print(f"Результат: {filters[int(i)]["function"](vvod)}")
    menu()
exit()