
"""Задание 3.
// Определить, какие из слов «attribute», «класс», «функция», «type»
// невозможно записать в байтовом типе с помощью маркировки b'' (без encode decode).
// Подсказки:
// --- используйте списки и циклы, не дублируйте функции
// --- обязательно!!! усложните задачу, "отловив" и обработав исключение,
// придумайте как это сделать
// """

FIRST_WORD = 'attribute'
SECOND_WORD = 'класс'
THIRD_WORD = 'функция'
FOURTH_WORD = 'type'
word_list = [FIRST_WORD, SECOND_WORD, THIRD_WORD, FOURTH_WORD]
for element in word_list:
    try:
        print(bytes(element, 'ascii'))
    except UnicodeEncodeError:
        print(f'Слово "{element}" невозможно записать в виде байтовой строки')