# this is the entry point to our web application.
# we call this app from the command line

# import the Flask class from the flask moodule
from flask import Flask


# instanciate the Flask class. The object name is app by convention
app = Flask(__name__) # the variable name is passed for initialization



# this command only starts the server. If you do not provide where the app should look into, it gives the "Not found" error
if __name__ == '__main__':
    # call the run method of the app object with the debug flag set as True
    app.run(debug=True)
