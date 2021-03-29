from flask import Flask, request, markup, render_template, flash, Markup
import os
import jason

app = Flask(__name__) 

@app.route('/')
def home():
    return render_template('random.html')
  
def get_state_options():
    listOfStates = []
    with open('county_demographics.json') as demographics_data:
        counties = json.load(demographics_data)
    for county in counties:
        if not(county["State"] in listOfStates): 
            listOfStates.append(county["State"])
  
if __name__=='__main__':
    app.run(debug=True)
