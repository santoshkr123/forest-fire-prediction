# 🔥 Forest Fire Prediction Web App
This is a Flask-based web application that predicts the Forest 𝗙𝗼𝗿𝗲𝘀𝘁 𝗙𝗶𝗿𝗲 𝗪𝗲𝗮𝘁𝗵𝗲𝗿 𝗜𝗻𝗱𝗲𝘅  (𝗙𝗪𝗜) using a 𝗥𝗶𝗱𝗴𝗲 𝗥𝗲𝗴𝗿𝗲𝘀𝘀𝗶𝗼𝗻 𝗺𝗼𝗱𝗲𝗹 trained on weather and forest data.

🚀 𝗙𝗲𝗮𝘁𝘂𝗿𝗲𝘀
- Predicts FWI based on 9 input parameters
- Scalable and responsive web interface using HTML templates
- Model and scaler are saved as `.pkl` files
- Easy to extend with other ML models or frontend frameworks


  📁 𝗣𝗿𝗼𝗷𝗲𝗰𝘁 𝗦𝘁𝗿𝘂𝗰𝘁𝘂𝗿𝗲
  ForestFireML/
│
├── models/
│ ├── ridge.pkl # Trained Ridge Regression model
│ └── scaler.pkl # StandardScaler used for preprocessing
│
├── templates/
│ ├── index.html # Input form page
│ └── home.html # Result display page
│
├── app.py # Main Flask app
├── README.md # Project documentation
└── requirements.txt # Python dependencies


---

## 🧠 Model Inputs

The following 9 features are used for prediction:

1. `Temperature`
2. `RH` (Relative Humidity)
3. `Ws` (Wind Speed)
4. `Rain` (Rainfall)
5. `FFMC` (Fine Fuel Moisture Code)
6. `DMC` (Duff Moisture Code)
7. `ISI` (Initial Spread Index)
8. `Classes` (Fire severity class as numeric)
9. `Region` (Region encoded as numeric)

𝗜𝗻𝘀𝘁𝗮𝗹𝗹 𝗱𝗲𝗽𝗲𝗻𝗱𝗲𝗻𝗰𝗶𝗲𝘀:
pip install -r requirements.txt

𝗥𝘂𝗻 𝘁𝗵𝗲 𝗮𝗽𝗽:
python app.py


𝗗𝗲𝗽𝗲𝗻𝗱𝗲𝗻𝗰𝗶𝗲𝘀
Make sure requirements.txt contains:
Flask
pandas
numpy
scikit-learn

  
