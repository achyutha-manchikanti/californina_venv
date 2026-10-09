from flask import Flask, redirect,url_for
app=Flask(__name__)

@app.route('/')
def greet():
    return('https://www.amazon.in/')
#here we are redirecting the webpage 
@app.route('/go_amazon')
def go_amazon():
    return(redirect("https://www.amazon.in/"))

@app.route('/third_party')
def third_party():
    return(redirect(url_for('go_amazon')))

if __name__=="__main__":
    app.run(debug=True)