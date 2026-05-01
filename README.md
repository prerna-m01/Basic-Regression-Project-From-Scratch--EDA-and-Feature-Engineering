# 📊 Basic Regression Project From Scratch — EDA & Feature Engineering

A beginner-friendly Machine Learning project focused on building regression models from scratch while performing complete Exploratory Data Analysis (EDA) and Feature Engineering using Python.

This project demonstrates the end-to-end workflow of a regression-based Machine Learning project, including:

* Data preprocessing
* Exploratory Data Analysis (EDA)
* Feature Engineering
* Model building
* Prediction and evaluation
* FastAPI integration
* Cloud deployment using Render

The primary goal of this project is to understand how regression algorithms work and how proper preprocessing and feature engineering improve model performance.

---

# 🚀 Project Overview

This repository contains implementations and experiments with:

* Simple Linear Regression
* Multiple Linear Regression
* Feature Engineering techniques
* Data Cleaning
* Visualization and statistical analysis
* Machine Learning model deployment using FastAPI

The project follows a complete practical Machine Learning pipeline:

1. Data Collection
2. Data Cleaning
3. Exploratory Data Analysis (EDA)
4. Feature Engineering
5. Model Training
6. Prediction
7. Model Evaluation
8. API Deployment

---

# 🌐 Live Deployment

## 🔗 Live API

[Open Live API](https://basic-regression-project-from-scratch.onrender.com)

## 📄 Interactive API Documentation

[Open Swagger Docs](https://basic-regression-project-from-scratch.onrender.com/docs)

The API documentation allows users to test regression prediction endpoints directly from the browser using FastAPI's interactive Swagger UI.

---

# 📂 Project Structure

```bash
Basic-Regression-Project/
│
├── data/
│   └── dataset.csv
│
├── notebooks/
│   └── regression_analysis.ipynb
│
├── models/
│   └── trained_model.pkl
│
├── images/
│   └── graphs.png
│
├── main.py
├── requirements.txt
├── .gitignore
└── README.md
```

---

# 🛠️ Technologies Used

* Python
* NumPy
* Pandas
* Matplotlib
* Seaborn
* Scikit-learn
* Jupyter Notebook
* FastAPI
* Uvicorn
* Render
* Git & GitHub

---

# 📊 Exploratory Data Analysis (EDA)

The project includes:

* Missing value analysis
* Correlation heatmaps
* Distribution plots
* Outlier detection
* Feature relationship analysis
* Statistical insights

EDA helps in understanding data patterns, correlations, and feature importance before training regression models.

---

# ⚙️ Feature Engineering

Feature engineering techniques used:

* Handling missing values
* Feature scaling
* Encoding categorical variables
* Outlier removal
* Feature selection
* Data preprocessing

These preprocessing steps improve model performance and prediction accuracy.

---

# 📈 Regression Models

This project explores:

* Simple Linear Regression
* Multiple Linear Regression

The models are trained and evaluated to understand how independent variables affect target predictions.

---

# ⚡ FastAPI Integration

The trained regression model was integrated with FastAPI to expose machine learning predictions through REST API endpoints.

Example endpoint:

```python
@app.get("/predict")
def predict(value: float):
```

Users can provide input values and receive predictions in JSON format.

---

# 📌 Example API Response

```json
{
  "input": 5,
  "prediction": 487.40469783807
}
```

---

# 🔄 Deployment Workflow

```text
User Input
   ↓
FastAPI API Endpoint
   ↓
Regression Model
   ↓
Prediction Response
```

The project was deployed using Render to make the ML model accessible online.

---

# ▶️ How to Run the Project Locally

## 1️⃣ Clone Repository

```bash
git clone https://github.com/prerna-m01/Basic-Regression-Project-From-Scratch--EDA-and-Feature-Engineering.git
```

---

## 2️⃣ Navigate to Project Folder

```bash
cd Basic-Regression-Project-From-Scratch--EDA-and-Feature-Engineering
```

---

## 3️⃣ Create Virtual Environment

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### macOS/Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## 4️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 5️⃣ Run FastAPI Application

```bash
uvicorn main:app --reload
```

---

## 6️⃣ Open API Documentation

```text
http://127.0.0.1:8000/docs
```

---

# 📷 Visualizations

The project includes:

* Scatter plots
* Regression plots
* Heatmaps
* Pair plots
* Distribution analysis

These visualizations help in understanding feature relationships and model behavior.

---

# 🎯 Learning Outcomes

Through this project, the following concepts were explored:

* End-to-end Machine Learning workflow
* Regression algorithms
* Data preprocessing
* Exploratory Data Analysis
* Feature Engineering
* Model evaluation
* FastAPI backend development
* REST API creation
* ML model deployment using Render

---

# 💡 Future Improvements

* Add Decision Tree Regression
* Add Random Forest Regression
* Add Streamlit frontend UI
* Dockerize the application
* Add model monitoring
* Improve API validation using Pydantic
* Deploy multiple ML models

---

# 🤝 Contributing

Contributions are welcome.

Feel free to fork this repository and improve the project.

---

# 👩‍💻 Author

**Prerna**

* GitHub: https://github.com/prerna-m01

---

# ⭐ Support

If you found this project useful, consider giving this repository a star.
