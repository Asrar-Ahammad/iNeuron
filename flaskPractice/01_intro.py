# Simple flask application

from flask import Flask,redirect,url_for,render_template,request

## Create the flask app

app = Flask(__name__) ## __name__ defines the entry point of the app. It is a parameter of entry point.
@app.route('/') # This is the decorator. refering to home page.
def home():
    return "hello world"

@app.route('/welcome')
def welcome():
    return "<h1>Hello world</h1>"

@app.route('/index')
def index():
    # return redirect(url_for('../templates/01_intro'))
    return render_template('01_intro.html')

@app.route('/success/<int:score>')
def success(score):
    return 'The person is passed and score is '+ str(score)
    
@app.route('/fail/<int:score>')
def fail(score):
    return 'The person is passed and score is '+ str(score)


@app.route('/calculate',methods=['POST','GET'])
def calculate():
    result = ''
    if request.method == 'GET':
        return render_template('calculate.html')
    else:
        maths = float(request.form['maths'])
        science = float(request.form['science'])
        history = float(request.form['history'])

        average_marks = (maths+science+history)/3
        # if average_marks >= 50:
        #     result='success'
        # else:
        #     result = 'fail'
    return render_template('result.html',results = average_marks)
        # return redirect(url_for(result, score=average_marks))
        # return render_template('result.html',results = average_marks)


if __name__ =='__main__': # This is the entry point.__name__ refers here.
    app.run(debug=True) # Debug =True should be done in only development.