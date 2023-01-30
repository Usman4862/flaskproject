from flask import Flask, render_template
import requests
app = Flask(__name__) # Project starts in this folder

@app.route("/") # decorator
def home_page():
    return render_template("pages/index.html")

@app.route("/album")
def album():
    return render_template("pages/album.html")

# /about --  
# render_template searches the files in the templates folder. which should be present in project folder
@app.route("/about")
def usman():
    return render_template("pages/about.html")

@app.route("/contact")
def my_contacts():
    list_of_students = [
        {
            "first_name": "Shahzaib",
            "last_name": "Akash"
        },
        {
            "first_name": "Usman",
            "last_name": "Malik"
        },
        {
            "first_name": "Mubashir",
            "last_name": "Rajput"
        }
    ]
    return render_template("pages/contact.html", students=list_of_students)



# /random_quote
@app.route("/randomqoute")
def randomqoute():
    result = requests.get(f"https://meowfacts.herokuapp.com/?count=1").json()
    x = result["data"][0]
    return render_template("pages/randomqoute.html", quote=x)


# Positional Arguments
# Keyword Argument