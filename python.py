from flask import Flask, request, markup, render_template, flash, Markup
import os
import jason

app = Flask(__name__) 

@app.route('/')
def home():
    return render_template('random.html', options=get_state())
  
def get_state_options():
    listOfStates = []
    with open('county_demographics.json') as demographics_data:
        counties = json.load(demographics_data)
    for county in counties:
        if not(county["State"] in listOfStates): 
            listOfStates.append(county["State"])
    options = ""
    for state in listOfStates:
        options = options + Markup("<option value=\"" + State + "\">" + State + "</option>")
    return options
  
if __name__=='__main__':
    app.run(debug=True)
