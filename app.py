

from flask import Flask, render_template, redirect
app = Flask(__name__)
from flask_pymongo import PyMongo

# @app.route('/')
# def hello_world():
#     return 'Hello, World!'@app.route('/')

@app.route("/")
@app.route("/home")
def home():
    return render_template("index.html")
    # Find one record of data from the mongo database
    # mars_info = mongo.db.collection.find_one()
    # print(mars_info)
    # Return template and data
    # , mars_info = mars_info, text = text 

if __name__ == "__main__":
    app.run(debug=True)