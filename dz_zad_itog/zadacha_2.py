"""Задание 2
// Каждое из слов «class», «function», «method» записать в байтовом формате
// без преобразования в последовательность кодов
// не используя!!! методы encode и decode)
// и определить тип, содержимое и длину соответствующих переменных.
// Подсказки:
// --- b'class' - используйте маркировку b''
// --- используйте списки и циклы, не дублируйте функции
"""



FIRST_WORD = b'class'
SECOND_WORD = b'function'
THIRD_WORD = b'method'
word_lst = [FIRST_WORD, SECOND_WORD, THIRD_WORD]
for element in word_lst:
    print(type(element))
    print(element)
    print(len(element))