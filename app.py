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

    with open("lokasi.txt", "a") as f:
        f.write(f"{time} - Lat: {lat}, Lon: {lon}\n")

    return {"status": "sukses"}

if __name__ == "__main__":
    app.run(debug=True)
