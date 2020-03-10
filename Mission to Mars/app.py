from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import play

# Create an instance of Flask
app = Flask(__name__)

# Use flask_pymongo to set up mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
mongo = PyMongo(app)

@app.route("/")
def index():
    new_data = mongo.db.data.find_one()
    return render_template("index.html", new_data=new_data)

@app.route("/scrape")
def scraper():
    mongo_data = mongo.db.data
    mars_data = play.scrape()
    mongo_data.update({}, mars_data, upsert=True)
    return redirect("/", code=302)

if __name__ == "__main__":
    app.run(debug=True,port=8005)   