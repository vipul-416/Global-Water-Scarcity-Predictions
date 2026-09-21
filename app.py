from flask import Flask, render_template, request
import pandas as pd
import pickle


with open("water_scarcity_model.pkl", "rb") as file:
    model = pickle.load(file)


app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")



@app.route("/predict", methods=["POST"])
def predict():
    try:

        country = request.form["country"]
        year = int(request.form["year"])
        total_water = float(request.form["total_water"])
        per_capita = float(request.form["per_capita"])
        agricultural = float(request.form["agricultural"])
        industrial = float(request.form["industrial"])
        household = float(request.form["household"])
        rainfall = float(request.form["rainfall"])
        groundwater = float(request.form["groundwater"])

        input_data = pd.DataFrame({
            "Country": [country],
            "Year": [year],
            "Total Water Consumption (Billion m3)": [total_water],
            "Per Capita Water Use (L/Day)": [per_capita],
            "Agricultural Water Use (%)": [agricultural],
            "Industrial Water Use (%)": [industrial],
            "Household Water Use (%)": [household],
            "Rainfall Impact (mm)": [rainfall],
            "Groundwater Depletion Rate (%)": [groundwater]
        })

        prediction = model.predict(input_data)[0]

        return render_template(
            "index.html",
            prediction_text=f"Predicted Water Scarcity Level: {prediction}"
        )

    except Exception as e:
        return render_template(
            "index.html",
            prediction_text=f"Error: {str(e)}"
        )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)