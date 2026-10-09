from flask import Flask,request
app=Flask(__name__)

@app.route('/')
def greet():
    return("Hello World")

@app.route('/add1')
def add1():
    a=10
    b=20
    return(f'the addition of {a} and {b} is :{a+b}')

@app.route('/add2/<a>/<b>')
def add2(a,b):
    return(f'the addition of {a} and {b} is :{a+b}')

@app.route('/add3/<int:a>/<int:b>')
def add3(a,b):
    return(f'the addition of {a} and {b} is :{a+b}')

@app.route('/add4')
def add4():
    a=request.args.get('number1',default=0,type=int)
    b=request.args.get('number2',default=0,type=int)
    return(f'the addition of {a} and {b} is :{a+b}')

if __name__=='__main__':
    app.run(debug=True)