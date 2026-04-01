from flask import Flask, render_template, request, jsonify, redirect, url_for
from flask_cors import CORS
import os
import logging

from src.pipeline.prediction_pipeline import PredictPipeline, CustomData

app = Flask(__name__, template_folder="templates", static_folder="static")
app.secret_key = os.environ.get("SECRET_KEY", "dev-secret")
CORS(app)

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/home", methods=["GET"])
def home():
    return render_template("home.html")

@app.route("/predict", methods=["POST"])
def predict():
    try:
        # Extract form data
        data = CustomData(
            loan_id=request.form.get("loan_id"),
            gender=request.form.get("gender"),
            married=request.form.get("married"),
            dependents=request.form.get("dependents"),
            education=request.form.get("education"),
            self_employed=request.form.get("self_employed"),
            applicantincome=float(request.form.get("applicantincome", 0)),
            coapplicantincome=float(request.form.get("coapplicantincome", 0)),
            loanamount=float(request.form.get("loanamount", 0)),
            loan_amount_term=float(request.form.get("loan_amount_term", 0)),
            credit_history=float(request.form.get("credit_history", 0)),
            property_area=request.form.get("property_area")
        )
        
        pred_df = data.get_data_as_data_frame()
        pipeline = PredictPipeline()
        prediction = pipeline.predict(pred_df)
        
        result = prediction[0] if hasattr(prediction, "__len__") else prediction
        return redirect(url_for("result", prediction=result))
    
    except Exception as e:
        logger.exception("Prediction failed")
        return jsonify({"error": str(e)}), 500

@app.route("/result", methods=["GET"])
def result():
    prediction = request.args.get("prediction", "No prediction")
    return render_template("result.html", prediction=prediction)

@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "ok"})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)