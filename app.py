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
    BuyOrRent = request.form.get('BuyOrRent')
    InvestmentOrLiveIn = request.form.get('InvestmentOrLiveIn')
    FrequencyOfTravel = request.form.get('FrequencyOfTravel')
    priceRange = request.form.get('PriceRange')
    bedrooms = request.form.get('bedrooms')
    Area = request.form.get('area')
    # smallSpace = request.form.get('smallSpace')
    # expenseRatio = request.form.get('expenseRatio')
    # savingsRatio = request.form.get('savingsRatio')
    Family = request.form.get('family')
    downtown = request.form.get('downtown')
    Social = request.form.get('social')
    daily = request.form.get('daily')

    print(BuyOrRent)
    print(InvestmentOrLiveIn)
    print(FrequencyOfTravel)
    print(priceRange)
    print(bedrooms)
    print(Area)
    print(Family)
    print(downtown)
    print(Social)
    print(daily)


    engine.reset()
    engine.get_rules()
    engine.declare(
    Property(buyOrRent=BuyOrRent),
    Property(InvestOrLivein=InvestmentOrLiveIn),
    Property(frequencyOfTravel=FrequencyOfTravel),
    Property(PriceRange=priceRange),
    Property(bedroom=bedrooms),
    Property(area=Area), 
    Property(family=Family), 
    Property(location=downtown),
    Property(social=Social),
    Property(dailyCommute=daily))
    engine.run()
    result=""
    with open('./res.txt') as f:
        result = f.readlines()
    return render_template('results.html', resultVal=result[0])

if __name__ == '__main__':
    app.run()