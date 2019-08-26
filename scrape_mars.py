# import necessary libraries
from flask import Flask, render_template, redirect, jsonify
from flask_pymongo import PyMongo
from scrapetest import scrape



# create instance of Flask app
app = Flask(__name__)


# Use PyMongo to establish Mongo connection
mongo = PyMongo(app, uri="mongodb://localhost:27017/mars_info_db")



# create route that renders index.html template
@app.route("/")
def index():
   mars_info = mongo.db.mars.find_one()
   # return render_template("index.html", mars_info=mars_info)
   #return jsonify({"key":"test scrape"})
   return jsonify(scrape())



@app.route("/scrape")
def scraper():
   mars = mongo.db.mars
   mars_dict = scrape()
   mars.update({}, mars_dict, upsert=True)
   return redirect("/", code=302)


if __name__ == "__main__":
    app.run(debug=True)

   

