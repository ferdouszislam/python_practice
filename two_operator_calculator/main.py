#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 28 20:30:27 2021

@author: demislam
"""


def add(a, b):
    return float(a) + float(b)


def minus(a, b):
    return float(a) - float(b)


def multiply(a, b):
    return float(a) * float(b)


def divide(a, b):
    return float(a) / float(b)


def process_input(user_input):

    invalid_format_err_msg = "invalid input format [format: 'number1 operator number2' with or without spaces]"

    for s_idx in range(0, len(user_input)):
        if (user_input[s_idx].isnumeric()
                or user_input[s_idx] == '.'
                or user_input[s_idx] == '+'
                or user_input[s_idx] == '-'
                or user_input[s_idx] == '*'
                or user_input[s_idx] == '/'):
            continue
        else:
            raise Exception(invalid_format_err_msg)

    if '+' in user_input:
        split_parts = user_input.split('+')
        result = add(split_parts[0], split_parts[1])

    elif '-' in user_input:
        split_parts = user_input.split('-')
        result = minus(split_parts[0], split_parts[1])

    elif '*' in user_input:
        split_parts = user_input.split('*')
        result = multiply(split_parts[0], split_parts[1])

    elif '/' in user_input:
        split_parts = user_input.split('/')
        result = divide(split_parts[0], split_parts[1])

    else:
        raise Exception(invalid_format_err_msg)

    print('>', result)


def main():
    print('press "q" to exit')

    while True:

        user_input = input()

        if user_input == 'q':
            break

        try:
            process_input(user_input)
        except Exception as exception:
            print(str(exception))

    print("ba bye!")


main()
