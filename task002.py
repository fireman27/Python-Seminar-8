"""Напишите функцию encrypt_caesar(msg, shift), которая кодирует сообщение шифром Цезаря и возвращает его. 
Шифр Цезаря заменяет каждую букву в тексте на букву, которая отстоит в алфавите на некоторое фиксированное число позиций.
В функцию передается сообщение и сдвиг алфавита. Если сдвиг не указан, то пусть ваша
функция кодирует сдвиг алфавита на 3 позиции:
А→Г,А→Г,
Б→Д,Б→Д,
В→Е,В→Е,
……
Э→А,Э→А,
Ю→Б,Ю→Б,
Я→ВЯ→В
Все символы, кроме русских букв должны остаться неизменными. Маленькие буквы должны превращаться в маленькие, 
большие — в большие. Напишите также функцию декодирования decrypt_caesar(msg, shift), также использующую сдвиг по умолчанию. 
При написании функции декодирования используйте вашу функцию кодирования."""

def encrypt_caesar(msg, shift):
    if msg.isalpha():
        number = ord(msg) + shift % 32
        if number > 1103:
            number -= 32
        return chr(number)
    return msg

shift = int(input('Шаг шифровки: ')) 
for l in input('Сообщение для шифровки: '): 
 print(encrypt_caesar(l, shift), end='') 
 
def decrypt_caesar(msg, shift):
    if msg.isalpha():
        number = ord(msg) - shift % 32
        if number > 1103:
            number -= 32
        return chr(number)
    return msg

