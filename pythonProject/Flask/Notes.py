'''
We'll sell some bacics of Flask here
the typical file structure for flask is        
    app.py
    requirements.txt
    templates > this folder contains all the HTML files we need to render our web pages.
    static > this folder contains all the static files we need to render our web pages like CSS, JS, images etc.
where app.py is the main file and requirements.txt is the file that contains all the packages we need to install for our project.
we can install flask using pip install flask
'''

from flask import Flask, render_template, request  # here we imported 'Flask' class from flassk module
#  render_template is used to render HTML templates, and request is used to handle incoming requests from the client.
#  Flask is a micro web framework for Python that allows us to build web applications quickly and easily. It is lightweight and easy to use, making it a popular choice for developers.

app = Flask(__name__)  # here we created an instance of the Flask class. The __name__ variable is a special built-in variable in Python that represents the name of the current module. When we run the script, __name__ will be set to "__main__". This allows Flask to know where to look for resources and templates.    

@app.route('/') # @app is a decorater which is a functin which contains another function. The route() function is used to bind a URL to a function. The '/' argument specifies the URL path that will trigger the function. In this case, it is the root URL of the application.
def index(): #this function will be called whanever the root URL (i.e. '/') is accessed.
    '''
    if name in request.args:
        name = request.args.get('name')
    else:
        name = 'world'
    '''
    # bot above and below cade are equivalent
    name = request.args.get('name', 'world')
    
    return render_template('index.html', name = name)
# this function will render the index.html file when the root URL is accessed. The render_template() function takes the name of the HTML file as an argument and returns the rendered HTML page. it automatically looks for the HTML file in the templates folder.

@app.route('/greet', methods=['POST']) # this route will be triggered when the form is submitted. The methods argument specifies that this route will only accept POST requests. we can add more medthos to it.
def greet():
    name =request.form.get('name', 'world') # here we are getting the name from the form data submitted by the user. The request.form object contains all the form data submitted by the user.
    # for get its args.get() and for post its form.get()
    # we can also use request.form['name'] but it will raise an error if the name is not found in the form data.
    # request.form.get() will return None if the name is not found in the form data.
    # we can also use request.form.get('name', 'world') to set a default value for the name if it is not found in the form data.
    return render_template('greet.html', name=name) # this function will render the greet.html file when the form is submitted. The render_template() function takes the name of the HTML file as an argument and returns the rendered HTML page. it automatically looks for the HTML file in the templates folder.


if __name__ == '__main__':
    app.run()