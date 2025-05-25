
from flask import Flask, request, jsonify
from threading import Thread
import time
import json

app = Flask(__name__)
filters = []

@app.route("/")
def home():
    return "Doginal Dog Sniper Backend Live"

@app.route("/alert", methods=["POST"])
def alert():
    data = request.json
    filters.append(data)
    print("Filter set:", data)
    return jsonify({"message": "Filter received", "filters": filters})

def scanner():
    while True:
        # Simulated listing from a real marketplace (replace this with actual fetch in future)
        sample_listing = {
            "id": "1337",
            "trait": "laser eyes",
            "price": 1350
        }

        for f in filters:
            matches = True
            if f.get("dogId") and f["dogId"] != sample_listing["id"]:
                matches = False
            if f.get("trait") and f["trait"].lower() not in sample_listing["trait"].lower():
                matches = False
            if f.get("maxPrice") and float(sample_listing["price"]) > float(f["maxPrice"]):
                matches = False

            if matches:
                print(f"** MATCH FOUND: {sample_listing} for filter {f} **")

        time.sleep(15)

Thread(target=scanner, daemon=True).start()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
