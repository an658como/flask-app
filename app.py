# this is the entry point to our web application.
# we call this app from the command line

# import the Flask class from the flask moodule
from pydoc import render_doc
from flask import Flask, render_template


# instanciate the Flask class. The object name is app by convention
app = Flask(__name__) # the variable name is passed for initialization

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
    return render_template('index.html', custom_input='Ali Naseri')

# this command only starts the server. If you do not provide where the app should look into, it gives the "Not found" error
# to avoid this issue, routers using decorators must be added before here
if __name__ == '__main__':
    # call the run method of the app object with the debug flag set as True
    app.run(debug=True)
