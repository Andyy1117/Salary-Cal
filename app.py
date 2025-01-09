from flask import Flask, render_template, request

app = Flask(__name__)

# Functions for calculations
def calculate_total_salary(days_worked, day_rate):
    return days_worked * day_rate

def calculate_late_penalty(late_time, minute_rate):
    return late_time * minute_rate

def calculate_tax(pretax_salary, tax_rate):
    return (pretax_salary * tax_rate) / 100

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # Get user inputs from the form
        days_worked = int(request.form["days_worked"])
        late_time = int(request.form["late_time"])

        day_rate = 300_000
        minute_rate = 400
        tax_rate = 13

        # Calculations using functions
        gross_salary = calculate_total_salary(days_worked, day_rate)
        late_penalty = calculate_late_penalty(late_time, minute_rate)
        pretax_salary = gross_salary - late_penalty
        tax_deduction = calculate_tax(pretax_salary, tax_rate)
        aftertax_salary = pretax_salary - tax_deduction

        # Pass results to the template
        return render_template(
            "index.html",
            gross_salary=gross_salary,
            late_penalty=late_penalty,
            pretax_salary=pretax_salary,
            tax_deduction=tax_deduction,
            aftertax_salary=aftertax_salary,
        )

    # Render form if it's a GET request
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
