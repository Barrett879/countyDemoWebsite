from flask import Flask, request, Markup, render_template, flash
import os
import json

app = Flask(__name__) 

@app.route('/')
def home():
    return render_template('home.html', options=get_state_options())

@app.route('/funFact', mthods=['GET', 'POST'])
def render_fun_fact():
    if request.method == "POST":
        state_chosen = request.form['states']
        return render_template('home.html', options=get_state_options(), funFact=fun_fact_by_state(state_chosen))
    else:
        return render_template('home.html', options=get_state_options())
  
def get_state_options():
    listOfStates = []
    with open('county_demographics.json') as demographics_data:
        counties = json.load(demographics_data)
    for county in counties:
        if not(county["State"] in listOfStates): 
            listOfStates.append(county["State"])
    options = ""
    for state in listOfStates:
        options = options + Markup("<option value=\"" + state + "\">" + state + "</option>")
    return options

def fun_fact_by_state(state):
    with open('county_demographics.json') as demographics_data:
        counties = json.load(demographics_data)
    first_county = "ZZZZZZZZ"
    for county in counties:
        if county["County"] < first_county and county["State"] == state:
            first_county = county["County"]
    return first_county
  
if __name__=='__main__':
    app.run(debug=True)
