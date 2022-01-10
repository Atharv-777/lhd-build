from flask import Flask, render_template, request
import requests, json

app = Flask(__name__)
app.config["DEBUG"] = True

@app.route('/', methods=['GET','POST'])
def index():
    desc=""
    temp=""
    humid=""
    city=""
    city, desc, temp,humid = "", "", "", ""
    if request.method == 'POST':
        city = request.form.get('city')
        baseUrl = "https://api.openweathermap.org/data/2.5/weather?q=" + city + "&appid=6371400a633f5f2f04681c5f5a04afa5"
        response = requests.get(baseUrl)
        result = response.json()
        desc = result['weather'][0]['description']
        kelvin = result['main']['temp']
        temp = int(kelvin - 273.15)
        humid = result['main']['humidity']
        # sealevel = result['main']['sea_level']
        # print(desc, temp, humid, sealevel)
        # print(type(result))
        # print(result)
    return render_template('index.html', city=city, desc=desc, temp=temp, humid=humid)

if __name__ == "__main__":
    app.run(debug=True, threaded=True)