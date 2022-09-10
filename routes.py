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

# routes are set to be compatible with GET by default. In case you need
# to includee POST, you should consider it in the route definition
# the actions must be provided in a list that is called methods
@app.route('/about', methods=['GET', 'POST'])
def about():
    form = forms.AddTaskForm()
    # now that the POST action is activated, we can have access to the forms data
    
    # check if the data exists:
    if form.validate_on_submit():
        # print the data on console
        print(form.title.data)
        # as an example pass the data back to the about form
        return render_template('about.html', form=form, title=form.title.data)
    return render_template('about.html', form=form)
