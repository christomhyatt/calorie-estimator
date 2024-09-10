from flask import Flask, render_template, request

app = Flask(__name__)

def CalorieEstimatorMetric(body_weight, distance, elevation_gain, expected_time_h):

   # Calculate calories burned
    flat_terrain_calories = body_weight * distance
    elevation = ((elevation_gain * 10)*.001) * body_weight                 
    burned_calories = round(flat_terrain_calories + elevation)

    # Caluclate calories to consume
    calorie_intake_hour = round((burned_calories / expected_time_h)*.3)
    carb_intake_hour = round(calorie_intake_hour / 4)

    return (f"The estimated number of calories you will burn during the race are <b>{burned_calories}</b>. "
            f"For every hour during the race, plan to consume <b>{calorie_intake_hour}</b> calories "
            f"or <b>{carb_intake_hour}</b> grams of carbohydrates.")

def CalorieEstimatorImperial(body_weight, distance, elevation_gain, expected_time_h):

    # Convert metric to imperial for sake of the formula
    body_weight_kg = body_weight / 2.20462
    distance_km = distance / 0.621371
    elevation_gain_me = elevation_gain * .305

    # Calculate calories burned
    flat_terrain_calories = body_weight_kg * distance_km
    elevation = ((elevation_gain_me * 10)*.001) * body_weight_kg                  
    burned_calories = round(flat_terrain_calories + elevation)

    # Caluclate calories to consume
    calorie_intake_hour = round((burned_calories / expected_time_h)*.3)
    carb_intake_hour = round(calorie_intake_hour / 4)

    return (f"The estimated number of calories you will burn during the race are <b>{burned_calories}</b>. "
            f"For every hour during the race, plan to consume <b>{calorie_intake_hour}</b> calories "
            f"or <b>{carb_intake_hour}</b> grams of carbohydrates.")

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        try:
            unit = request.form.get('units')

            # Get input from the form
            body_weight = float(request.form['body_weight'].replace(',', ''))
            distance = float(request.form['distance'].replace(',', ''))
            elevation_gain = float(request.form['elevation_gain'].replace(',', ''))
            expected_time_h = float(request.form['expected_time_h'].replace(',', ''))

            if unit == "imperial":
                # Call the calculator function
                result = CalorieEstimatorImperial(body_weight, distance, elevation_gain, expected_time_h)
            else: 
                result = CalorieEstimatorMetric(body_weight, distance, elevation_gain, expected_time_h)
                
        except:
            result = "Please enter valid numeric values for all fields."

    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
