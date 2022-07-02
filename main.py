from flask import Flask, render_template, request
import requests, json, datetime
from geopy.geocoders import Nominatim 

app = Flask(__name__)
@app.route('/')
def index():
    return render_template ("index.html")

@app.route('/Proyecto1', methods=['POST', 'GET'])
def proyecto1():
    loc = Nominatim(user_agent="GetLoc")
    ciudad = request.form.get('nc')
    getLoc = loc.geocode(ciudad)
    url = "https://api.openweathermap.org/data/2.5/weather"
    querystring = {"lat":getLoc.latitude,"lon":getLoc.longitude,"appid":"0edbb152bdb614aedd0cdde4c4923185","units":"metric","lang":"38"}
    headers = {'Cache-Control': 'no-cache'}
    response = requests.request("GET", url, headers=headers, params=querystring)
    data = json.loads(response.content)

    hora_UTC = datetime.datetime.fromtimestamp(data['dt'])
    amanecer = datetime.datetime.fromtimestamp(data['sys']["sunrise"])
    atardecer = datetime.datetime.fromtimestamp(data['sys']["sunset"])

    dataTime = {
        "horaActual": hora_UTC.strftime('%d-%m-%Y %H:%M:%S'),
        "amanecer": amanecer.strftime('%H:%M:%S'),
        "atardecer": atardecer.strftime('%H:%M:%S'),
        "direccion": getLoc.address
    }

    return render_template ("proyecto1.html", data=data, dataTime=dataTime)

if __name__ == "__main__":
    app.run(debug=True)