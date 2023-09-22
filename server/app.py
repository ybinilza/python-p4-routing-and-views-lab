#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

if __name__ == '__main__':
    app.run(port=5555, debug=True)


@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'


@app.route('/print/<parameter>')
def print_string(parameter):
    print(f'{parameter}')
    return(f'{parameter}')

@app.route('/count/<int:parameter>')
def count(parameter):
    i=0;
    ans=""
    while(i<parameter):
        ans=ans+str(i)+"\n";
        i=i+1
    print(f'{ans}')
    return f'{ans}'


@app.route('/math/<int:num1>/<operation>/<int:num2>')
def math(num1,operation,num2):
    ans=0;
    if operation == "+":
        ans=num1+num2
    elif operation == "-":
        ans=num1-num2
    elif operation == "*":
        ans=num1*num2
    elif operation == "div":
        ans=num1/num2
    elif operation == "%":
        ans=num1%num2
    
    print(f'{ans}')
    return f'{ans}'
