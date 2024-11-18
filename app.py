from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello_world():

    return "<p>Hello, World!</p>"

@app.route("/products")
def products():
    return 'This is products page'


if __name__=='__main__':
    app.run(debug=True,port = 8000)