from flask import Flask, request, url_for, redirect, render_template, jsonify
import pickle
import json
import numpy as np
from model.ExpertSystems import PropertyRecommender, Property


app =Flask(__name__)

engine = PropertyRecommender()
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/propertyRecommender', methods=['POST'])
def predict():
    engine.reset()
    engine.get_rules()
    fromForm = request.form.get('BuyOrRent')
    engine.declare(Property(input='Buy, 4, 3, 1, NoDowntown'))
    engine.run()
    result=""
    with open('./res.txt') as f:
        result = f.readlines()
    return render_template('results.html', resultVal=result[0])

if __name__ == '__main__':
    app.run()