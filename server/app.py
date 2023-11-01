#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "<h1>Python Operations with Flask Routing and Views</h1>"

@app.route('/print/<string:parameter>')
def print_string(parameter):
    print(parameter)
    return parameter

@app.route('/count/<int:parameter>')
def count(parameter):
    number = []
    for i in range(parameter):
        number.append(f'{i}\n')
    return ''.join(number)

@app.route('/math/<num1>/<operator>/<num2>')
def math(num1,operator,num2):
    num1_int = int(num1)
    num2_int = int(num2)
    if operator == '+':
        return f'{num1_int + num2_int}'
    elif operator == '-':
        return f'{num1_int - num2_int}'
    elif operator == '*':
        return f'{num1_int * num2_int}'
    elif operator == 'div':
        return f'{num1_int / num2_int}'
    elif operator == '%':
        return f'{num1_int % num2_int}'
    else:
        return 'Oops'

if __name__ == '__main__':
    app.run(port=5555, debug=True)
