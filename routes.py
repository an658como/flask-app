# from app module, import the app instance
from app import app
from flask import render_template
import forms



# this points to the root folder of the server
# multiple decorators can be used for a function
@app.route('/')
@app.route('/index')
# exectue the following function
def index():
    # the return value of the function can be a simple string
    # return 'Hello world, Ali is in Canada!'
    
    # the return value of the function can be an html string
    # return '<h1>Welcome to my website!\n</h1><h2>my name is Ali Naseri</h2>'
    
    # the return value of the function can be an html template
    # return render_template('index.html')

    # the return value of the function can be an html template and an input
    return render_template('index.html')


@app.route('/about')
def about():
    form = forms.AddTaskForm()
    return render_template('about.html', form=form)
