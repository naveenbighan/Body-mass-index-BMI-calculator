from flask import Flask, render_template, request

app = Flask(__name__)

def calculate_bmi(weight, height):
    """Function to calculate BMI."""
    bmi = weight / (height / 100) ** 2
    return round(bmi, 2)

def bmi_category(bmi):
    """Function to determine BMI category."""
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight You need to do exercise daily"
    else:
        return "Obese"

@app.route("/", methods=["GET", "POST"])
def index():
    bmi = None
    category = None

    if request.method == "POST":
        try:
            weight = float(request.form["weight"])
            height = float(request.form["height"])
            
            bmi = calculate_bmi(weight, height)
            category = bmi_category(bmi)
        except ValueError:
            bmi = "Invalid input, please enter numbers only."

    return render_template("index.html", bmi=bmi, category=category)

if __name__ == "__main__":
    app.run(debug=True)
