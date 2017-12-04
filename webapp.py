from flask import Flask, url_for, render_template, request, Markup
import os
import json

app = Flask(__name__)

@app.route("/")
def render_main():
    return render_template('index.html')

@app.route("/most_delays")
def render_meter():
    with open('static/airlines.json') as airlines_data:
        airlines = json.load(airlines_data)
    if 'Airport' in request.args:
        selected_airport = request.args['Airport']
        return render_template('most_delays.html', response_airport_list = get_airport_list(airlines), response_airport = selected_airport, response_delays = get_airport_delays(airlines, selected_airport))
    return render_template('most_delays.html', response_airport_list = get_airport_list(airlines))

def get_airport_list(airlines):
    airports = []
    airport_list = ""
    for a in airlines:
        if a["airport"]["name"] not in airports:
            airports.append(a["airport"]["name"])
            airport_list += Markup("<option value=\"" + a["airport"]["name"] + "\">" + a["airport"]["name"] + "</option>")
    return airport_list

def get_airport_delays(airlines, airport):
    total_delays = 0
    for a in airlines:
        if a["airport"]["name"] == airport:
            total_delays += 5
    return total_delays


if __name__=="__main__":
    app.run(debug=True, port=54321)
