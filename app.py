from flask import Flask, render_template, request
import requests


import config
api_key = config.API_KEY


app = Flask(__name__)

def get_weather_results(zip_code):
    api_url = f'http://api.openweathermap.org/data/2.5/weather?zip={zip_code},pl&units=metric&appid={api_key}'
    response = requests.get(api_url)
    return(response.json())

@app.route('/')
def weather_dashboard():
    return render_template('home.html')


@app.route('/results', methods=['POST'])
def render_results():
    zip_code = request.form['zipCode']

    data = get_weather_results(zip_code)
    temp = "{0:.2f}".format(data["main"]["temp"])
    feels_like =  "{0:.2f}".format(data["main"]["feels_like"])
    weather = data["weather"][0]["main"]
    location = data["name"]
    icon = data["weather"][0]["icon"] 
    return render_template('results.html', temp=temp, feels_like=feels_like, weather=weather, location=location, icon_url=f'http://openweathermap.org/img/wn/{icon}@2x.png')




if  __name__ == '__main__':
    app.run(debug=True)





#get_weather_results('36-007')

