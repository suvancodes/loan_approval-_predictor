import os
import logging
from flask import Flask, render_template, request, jsonify, redirect, url_for
from flask_cors import CORS

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
        # Extract form data and match CustomData parameter names
        data = CustomData(
            Gender=request.form.get("Gender"),
            Married=request.form.get("Married"),
            Education=request.form.get("Education"),
            Self_Employed=request.form.get("Self_Employed"),
            ApplicantIncome=float(request.form.get("ApplicantIncome", 0)),
            CoapplicantIncome=float(request.form.get("CoapplicantIncome", 0)),
            LoanAmount=float(request.form.get("LoanAmount", 0)),
            Loan_Amount_Term=float(request.form.get("Loan_Amount_Term", 0)),
            Credit_History=float(request.form.get("Credit_History", 0))
        )
        
        pred_df = data.get_data_as_dataframe()
        pipeline = PredictPipeline()
        prediction = pipeline.predict(pred_df)
        
        # Convert prediction to simple 0 or 1
        result = int(prediction[0]) if hasattr(prediction, "__len__") else int(prediction)
        
        return redirect(url_for("result", prediction=result))
    
    except Exception as e:
        logger.exception("Prediction failed")
        return jsonify({"error": str(e)}), 500

@app.route("/result", methods=["GET"])
def result():
    prediction = request.args.get("prediction", "0")
    return render_template("result.html", prediction=prediction)

@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "ok"})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)