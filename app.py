from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# ✅ HOME ROUTE
@app.route("/")
def home():
    return render_template("index.html")


# ✅ ANALYZE ROUTE
@app.route("/analyze", methods=["POST"])
def analyze():
    data = request.get_json()
    text = data.get("symptom", "").lower()

    if "bleed" in text:
        return jsonify({"type": "bleeding"})
    elif "burn" in text:
        return jsonify({"type": "burns"})
    elif "heart" in text or "chest" in text:
        return jsonify({"type": "cardiac"})
    elif "choke" in text:
        return jsonify({"type": "choking"})
    elif "fracture" in text or "bone" in text:
        return jsonify({"type": "fracture"})
    else:
        return jsonify({"type": "unknown"})


if __name__ == "__main__":
    app.run(debug=True)