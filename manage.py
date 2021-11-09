from flask import Flask, render_template, render_template_string, request
import requests, os 
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")

app = Flask(__name__)

@app.route('/', methods=[ "GET", "POST" ])
def index():
    if request.method == "POST":               
        city_name = request.form.get("cityName")               
        response = requests.get(f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_KEY}")         
        json_obj = response.json()
                
        if json_obj["cod"] == 200:   
            content = {}          
            content["temp"] = "{:0.2f}".format(json_obj["main"]["temp"] - 273.15)            
            content["feels_like"] = "{:0.2f}".format(json_obj["main"]["feels_like"] - 273.15)            
            content["temp_max"] = "{:0.2f}".format(json_obj["main"]["temp_max"] - 273.15)            
            content["temp_min"] = "{:0.2f}".format(json_obj["main"]["temp_min"] - 273.15)            
            content["pressure"] = "{:0.2f}".format(json_obj["main"]["pressure"])
            content["humidity"] = "{:0.2f}".format(json_obj["main"]["humidity"])
            return render_template('result.html', content=content)
        
        else:
            return render_template_string(
                """
                <!DOCTYPE html>
                <html>
                <head>
                    <style>
                        h1 {
                            font-size:40px;
                        }
                        p {
                            font-size: 25px;
                        }
                    </style>
                    <title>Error Page</title>
                </head>
                <body>
                    <h1>404</h1>
                    <p><strong>Error:</strong> City not found! Check if city's name is correct or not... </p>    
                </body>
                </html>
                """
            )
    else:
        return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)