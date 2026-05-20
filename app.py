from flask import Flask, render_template, request
import joblib
import os

app = Flask(__name__)

model = joblib.load(os.path.join("model", "spam_model.pkl"))

@app.route("/", methods=["GET", "POST"])
def index():
    prediction = None
    confidence = None
    message = ""

    if request.method == "POST":
        message = request.form.get("message", "")
        if message.strip():
            prob = model.predict_proba([message])[0]
            pred = model.predict([message])[0]
            confidence = round(max(prob) * 100, 2)
            prediction = "SPAM" if pred == 1 else "NOT SPAM"

    return render_template(
        "index.html",
        prediction=prediction,
        confidence=confidence,
        message=message
    )

if __name__ == "__main__":
    app.run(debug=True)