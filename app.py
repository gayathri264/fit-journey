from flask import Flask, render_template, request, redirect, url_for  # pyright: ignore[reportMissingImports]
import os

app = Flask(__name__)

@app.route('/')
def login():
    return render_template("login.html")

@app.route('/home', methods=['POST'])
def home():
    name = request.form.get("name")
    return render_template("home.html", name=name)

@app.route('/calculate', methods=['POST'])
def calculate():
    try:
        weight = float(request.form['weight'])
        height = float(request.form['height']) / 100
        bmi = round(weight / (height ** 2), 2)
        category = classify_bmi(bmi)
        return render_template('result.html', bmi=bmi, category=category)
    except:
        return "Invalid input."

def classify_bmi(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25:
        return "Healthy"
    elif bmi < 30:
        return "Overweight"
    else:
        return "Obese"

@app.route('/diet')
def diet():
    # Simulated diet plan
    meals = {
        "Breakfast": "Oats with banana and nuts",
        "Lunch": "Grilled chicken salad",
        "Dinner": "Vegetable soup and brown rice",
        "Snacks": "Fruit bowl"
    }
    return render_template('diet.html', meals=meals)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
