def error(text, symbol, number):
    global errors
    print(text, symbol, number)
    errors += 1


def read():
    global number, symbol
    number += 1
    symbol = string[number]


def begin():
    read()
    main_choose()
    if symbol == '#':
        return
    else:
        error('begin', symbol, number)


def main_choose():
    if symbol == '(':
        expression_circle()
    elif symbol == '[':
        expression_square()
    elif symbol in alphabet:
        letter()
    else:
        error('main_choose', symbol, number)


def letter():
    if symbol in alphabet:
        read()
    else:
        error('letter', symbol, number)


def operation():
    if symbol in operations:
        read()
    else:
        error('operation', symbol, number)


def expression_circle():
    if symbol == '(':
        expression()
        if symbol == ')':
            read()
        else:
            error('expression_circle', symbol, number)
    else:
        error('expression_circle', symbol, number)


def expression_square():
    if symbol == '[':
        expression()
        if symbol == ']':
            read()
        else:
            error('expression_square', symbol, number)
    else:
        error('expression_square', symbol, number)


def expression():
    read()
    if symbol == '(':
        expression_circle()
        additional_circle()
    elif symbol == '[':
        expression_square()
        additional_square()
    elif symbol in alphabet:
        letter()
        operation()
        main_choose()
    else:
        error('expression', symbol, number)


def additional_circle():
    if symbol in operations:
        operation()
        next_square()


def additional_square():
    if symbol in operations:
        operation()
        next_circle()


def next_circle():
    if symbol in alphabet:
        letter()
    elif symbol == '(':
        expression_circle()
    else:
        error('next_circle', symbol, number)


def next_square():
    if symbol in alphabet:
        letter()
    elif symbol == '[':
        expression_square()
    else:
        error('next_square', symbol, number)


print("Enter a bracket expression:")

alphabet = 'abcdefghijklmnopqrstuvwxyz'
operations = '+-*/'

string = input()
string += '#'

number = -1
symbol = ''

errors = 0


begin()
if errors > 0:
    print("Invalid expression")
input("press any key to exit...")
