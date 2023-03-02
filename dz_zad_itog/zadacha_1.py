"""Задание 1.
// Каждое из слов «разработка», «сокет», «декоратор» представить
// в буквенном формате и проверить тип и содержание соответствующих переменных.
// Затем с помощью онлайн-конвертера преобразовать
// в набор кодовых точек Unicode (НО НЕ В БАЙТЫ!!!)
// и также проверить тип и содержимое переменных.
// Подсказки:
// --- 'разработка' - буквенный формат
// --- '\u0440\u0430\u0437\u0440\u0430\u0431\u043e\u0442\u043a\u0430' - набор кодовых точек
// --- используйте списки и циклы, не дублируйте функции
// """

FIRST_WORD = 'разработка'
SECOND_WORD = 'сокет'
THIRD_WORD = 'декоратор'
word_lst = [FIRST_WORD, SECOND_WORD, THIRD_WORD]
for element in word_lst:
    print(element)
    print(type(element))

FIRST_UNIC = '\u0440\u0430\u0437\u0440\u0430\u0431\u043e\u0442\u043a\u0430'
SECOND_UNIC = '\u0441\u043e\u043a\u0435\u0442'
THIRD_UNIC = '\u0434\u0435\u043a\u043e\u0440\u0430\u0442\u043e\u0440'
unic_lst = [FIRST_UNIC, SECOND_UNIC, THIRD_UNIC]
for element in unic_lst:
    print(element)
    print(type(element))