from pprint import pprint

def custom_write(file_name,strings):
    string_position = {} # Пустой словарь для возврата
    with open(file_name, 'w', encoding='utf-8') as file: # С помощью with потому что меньше строк кода писать
        for i,s in enumerate(strings,start = 1): # Перебираем  список info
            pos = file.tell() # позиция указателя
            file.write(s + '\n') # Пишет что перебралось в переменную цикла и переносит на новую строку
            string_position[(i,pos)] = s # i из списка info + позиция курсора
    return string_position #возврат


info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
  print(elem)



