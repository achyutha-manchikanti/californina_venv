from flask import Flask # step 1
app=Flask(__name__) # step2
@app.route('/') # decorating the flask page
def greet():
    return('welcome')
@app.route('/greet1')
def greet1():
    return('good morning')

if __name__=='__main__':
    app.run(host='0.0.0.0',port='8000',debug=True)

