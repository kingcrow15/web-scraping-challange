from flask import Flask 
from flask import render_template
from flask import redirect
from flask import request
from flask_pymongo import PyMongo
import scrapeData
from pymongo import MongoClient
import pymongo


app = Flask(__name__)

app.config["MONGO_URI"] = "mongodb://localhost:27017/mars"
mongo = PyMongo(app)

@app.route("/")
def index():

    mars = mongo.db.mars.find_one()
    
    return render_template("index.html", mars = mars)

 
@app.route("/scrape")
def scrape():

    mars = mongo.db.mars
    mars_web = scrapeData.scrape_news()
    mars_web = scrapeData.scrape_Img()
    mars_web = scrapeData.scrape_marsFact()
    mars_web = scrapeData.scrape__hemispheres()
    mars_web = scrapeData.scrape_Weather()
    
    
    mars.update({}, mars_web, upsert=True)
    
    return redirect("/", code=302)

if __name__ == "__main__":
    app.run(debug=True)