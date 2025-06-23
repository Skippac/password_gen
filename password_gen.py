
from random import choices

def get_positive_int(prompt):
    while True:
        user_input = input(prompt)
        if user_input.isdigit() and int(user_input) > 0:
            return int(user_input)
        print('Ошибка: введите целое число больше 0.')

def ask_yes_no(promt):
    while True:
        answer = input(promt + '(да/нет): ').strip().lower()
        if answer in ('да', 'д', 'yes' , 'y'):
            return True
        elif answer in ('нет', 'н', 'no' , 'n'):
            return False
        else:
            print('Ошибка: введите да или нет.')

def remove_ambiguous(charset):
    ambiguous = 'il1Lo0O'
    return ''.join(c for c in charset if c not in ambiguous)

def get_charset():
    digits = '0123456789'
    lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
    uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    punctuation = '!#$%&*+-=?@^_'
    while True:
        charset = ''
        if ask_yes_no('Используем числа в пароле?'):
            charset += digits
        if ask_yes_no('Используем строчные буквы?'):
            charset += lowercase_letters
        if ask_yes_no('Используем прописные буквы?'):
            charset += uppercase_letters
        if ask_yes_no('Используем спецсимоволы?'):
            charset += punctuation
        if ask_yes_no('Исключить неоднозначные символы(il1Lo0O)?'):
            charset = remove_ambiguous(charset)
        if not charset:
            if ask_yes_no('Ни один параметр не выбран,генерация не возможна.Попробуем снова или завершим?'):
                continue
            else:
                print('Программа завершена.')
                exit()
        else:
            break
    return charset

def generate_passwords(charset, length, amount):
    return [''.join(choices(charset,k = length)) for _ in range(amount)]


amount_passwords = get_positive_int('Введите количество паролей для генерации: ')
password_length = get_positive_int('Введите длинну одного пароля: ')
char = get_charset()

for i, pwd in enumerate(generate_passwords(char, amount_passwords, password_length), 1):
    print(f'Пароль {i}: {pwd}')


