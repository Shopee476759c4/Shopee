from flask import Flask, request, render_template
import datetime

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/location", methods=["POST"])
def location():
    data = request.get_json()
    lat = data.get("latitude")
    lon = data.get("longitude")
    time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    print(f"[{time}] Lokasi diterima: Latitude: {lat}, Longitude: {lon}")

    # Cetak ke log saja, karena file tidak persist di render
    return {"status": "sukses"}

if __name__ == "__main__":
    app.run()
