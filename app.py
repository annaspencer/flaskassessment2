from flask import Flask, render_template, request, jsonify 
from random import randint
import requests

app = Flask(__name__)
app.config['WTF_CSRF_ENABLED'] = False
app.config['SECRET_KEY'] = "105-919-298"

@app.route("/")
def homepage():
    """Show homepage."""

    return render_template("index.html")

@app.route("/api/get-lucky-num", methods=["POST"])
def get_lucky_num():
    """takes data from form, makes api call, returns lucky number information.

    Returns JSON {'num': {fact, num} 'year': {fact, year}}
    """
    
    
    
    # email = request.json["email"]
    year = request.json['year']
    
    # color = request.json["color"]
    num = randint(0,100)

    resp = requests.get(f"http://numbersapi.com/{num}?json")
    resp2 = requests.get(f"http://numbersapi.com/{year}/year?json")

    to_json = resp.json()
    to_json2 = resp2.json()

    response= {
        "num": { 
            "fact":to_json['text'],
            "num":num
        },
        "year": {
            "fact":to_json2['text'],
            "year": year
        } 
    }

   

    return jsonify(response)

   
        
    
    
