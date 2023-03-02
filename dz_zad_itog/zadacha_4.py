"""
Задание 4.
Преобразовать слова «разработка», «администрирование», «protocol»,
«standard» из строкового представления в байтовое и выполнить
обратное преобразование (используя методы encode и decode).
Подсказки:
--- используйте списки и циклы, не дублируйте функции
"""

FIRST_WORD = 'разработка'
SECOND_WORD = 'администрирование'
THIRD_WORD = 'protocol'
FOURTH_WORD = 'standard'
word_lst = [FIRST_WORD, SECOND_WORD, THIRD_WORD, FOURTH_WORD]
bytes_lst = []
for element in word_lst:
    bytes_num = element.encode('utf-8')
    print(bytes_num)
    bytes_lst.append(bytes_num)