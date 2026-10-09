from flask import Flask # step 1
# we need to create an app instance
app=Flask(__name__) # step2
@app.route('/') # decorating the flask page
def greet():
    return('welcome')
@app.route('/greet1')
def greet1():
    return('good morning')

if __name__=='__main__':
    app.run(debug=True)

