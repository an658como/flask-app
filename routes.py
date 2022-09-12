# from app module, import the app instance
#                , import the db instace
from app import app, db
# form flask module, import two other functions for URL and Redirecting
from flask import render_template, redirect, url_for
import forms
# from module models, import the Task class for your data model
from models import Task
# from module datetime, import datetime
from datetime import datetime

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

    # Query the Task class for the stored information and print them on the index page
    tasks_list = Task.query.all()
    return render_template('index.html', tasks=tasks_list)

# routes are set to be compatible with GET by default. In case you need
# to includee POST, you should consider it in the route definition
# the actions must be provided in a list that is called methods
@app.route('/add', methods=['GET', 'POST'])
def add():
    form = forms.AddTaskForm()
    # now that the POST action is activated, we can have access to the forms data
    
    # check if the data exists:
    if form.validate_on_submit():
        # create an instance of the Task class for storing the data
        t = Task(title=form.title.data, date=datetime.utcnow())
        db.session.add(t)
        db.session.commit()
        # return to the index page after recieving data
        return redirect(url_for('index'))
    return render_template('add.html', form=form)
